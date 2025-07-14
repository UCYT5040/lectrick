from PIL import Image, ImageDraw
from numpy import argwhere as np_argwhere
from numpy import array as np_array

from .crop_image import crop_image
from .font import get_font_for_character
from .tiles import get_sample_chars


def generate_svg(image, shape_name: str):
    width, height = image.size
    svg_content = f'<svg version="1.1" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'

    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            fill = f'rgb({pixel_value}, {pixel_value}, {pixel_value})' if pixel_value < 255 else 'white'
            svg_content += f'<rect x="{x}" y="{y}" width="1" height="1" fill="{fill}"/>'

    svg_content += '</svg>'

    with open(f'shapes/{shape_name}.svg', 'w') as svg_file:
        svg_file.write(svg_content)


def generate_shape(sample_characters: list[str], shape_name: str, generate_each_character: bool = False):
    max_width = 0
    max_height = 0
    for char in sample_characters:
        bbox = get_font_for_character(char).getbbox(char)
        char_width = bbox[2] - bbox[0]
        char_height = bbox[3] - bbox[1]
        max_width = max(max_width, char_width)
        max_height = max(max_height, char_height)

    image = Image.new('L', (max_width, max_height), 255)

    ink = 255 / len(sample_characters)  # To draw, subtract existing pixel value by this amount

    for i, char in enumerate(sample_characters):
        font = get_font_for_character(char)
        bbox = font.getbbox(char)
        char_x = -bbox[0]
        char_y = (max_height - (bbox[3] - bbox[1])) / 2 - bbox[1]
        char_image = Image.new('L', (max_width, max_height), 255)
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((char_x, char_y), char, font=font, fill=0)
        char_image = crop_image(char_image)
        char_image = char_image.resize(image.size, Image.Resampling.LANCZOS)
        char_image_width, char_image_height = char_image.size
        for x in range(char_image_width):
            for y in range(char_image_height):
                pixel_value = char_image.getpixel((x, y))
                main_image_change = (255 - pixel_value) / 255 * ink * -1
                current_pixel_value = image.getpixel((x, y))
                new_pixel_value = max(0, current_pixel_value + main_image_change)
                image.putpixel((x, y), int(new_pixel_value))

        if generate_each_character:
            bbox = char_image.getbbox()
            if bbox:
                char_image.save(f"shapes/{shape_name}_char{i}.png")

    # Crop the image to the bounding box of the drawn characters
    bbox = image.getbbox()
    if not bbox:
        print(f"No characters drawn for {shape_name}. Skipping.")
        return

    image_array = np_array(image)

    non_white_mask = image_array < 255

    non_white_pixels = np_argwhere(non_white_mask)

    if non_white_pixels.size == 0:
        print(f"No non-white pixels found for {shape_name}. Skipping.")
        return

    top, left = non_white_pixels.min(axis=0)
    bottom, right = non_white_pixels.max(axis=0) + 1  # +1 to include the last pixel

    image = image.crop((left, top, right, bottom))

    if image.size == (0, 0):
        print(f"Generated image for {shape_name} is empty. Skipping.")
        return

    # Save the image as a PNG file
    image.save(f"shapes/{shape_name}.png")

    # Generate SVG representation
    generate_svg(image, shape_name)


def generate_shapes(generate_each_character: bool = False):
    for shape_name, sample_chars in get_sample_chars():
        if len(sample_chars) == 0:
            continue
        generate_shape(sample_chars, shape_name, generate_each_character)
