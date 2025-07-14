from os.path import join

from PIL import Image, ImageDraw
from unicodedata import name as unicode_name

from .crop_image import crop_image
from .font import get_font_for_character
from .tiles import list_tile_types

OVERLAY_DIRECTORY = 'overlays'


def generate_overlays(char: str):
    print("Overlay Color Key:")
    # We add the shape pixel value to the R channel
    # and the character pixel value to the G channel
    # and the blue channel is set to 255
    print("Yellow: Shape & character match")
    print("Red: Shape has ink, character does not")
    print("Green: Character has ink, shape does not")

    tile_types = list_tile_types()

    for shape_name in tile_types:
        try:
            shape_image = Image.open(f"shapes/{shape_name}.png").convert('L')
        except FileNotFoundError:
            print(f"Shape for '{shape_name}' not found, skipping.")
            continue

        font = get_font_for_character(char)
        bbox = font.getbbox(char)
        if not (bbox and bbox[2] > bbox[0] and bbox[3] > bbox[1]):
            continue  # Skip characters with no visible glyph

        char_img = Image.new('L', (bbox[2] - bbox[0], bbox[3] - bbox[1]), 255)
        draw = ImageDraw.Draw(char_img)
        draw.text((-bbox[0], -bbox[1]), char, font=font, fill=0)

        # Crop and resize the character image to match the shape's dimensions
        char_img = crop_image(char_img)
        char_img = char_img.resize(shape_image.size, Image.Resampling.LANCZOS)

        # Create a new blank image for the overlay with an RGB color model
        overlay_image = Image.new('RGB', shape_image.size, (255, 255, 255))

        # Get pixel data for efficient access
        shape_pixels = shape_image.load()
        char_pixels = char_img.load()
        overlay_pixels = overlay_image.load()

        width, height = shape_image.size
        for x in range(width):
            for y in range(height):
                shape_val = shape_pixels[x, y]
                char_val = char_pixels[x, y]
                color = (255 - shape_val, 255 - char_val, 0)
                overlay_pixels[x, y] = color

        try:
            char_unicode_name = unicode_name(char)
        except TypeError:
            char_unicode_name = f"char_ord_{ord(char)}"

        output_filename = f"{shape_name}_{char_unicode_name}.png"
        output_path = join(OVERLAY_DIRECTORY, output_filename)
        overlay_image.save(output_path)
