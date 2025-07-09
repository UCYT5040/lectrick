from font import font
from PIL import Image, ImageDraw

WIDTH = 4
HEIGHT = 5


def char_image(char):
    metrics = font.getmetrics()
    bbox = font.getbbox(char)

    # Calculate the width and height of the character's bounding box
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]

    # Scale image width to character width and calculate height from the aspect ratio
    width = char_width
    height = int(width * HEIGHT / WIDTH)

    # Create a drawing context
    image = Image.new('L', (width, height), 255)  # Create a white image
    draw = ImageDraw.Draw(image)

    # Calculate the coordinates to center the character
    # The x-coordinate aligns the left of the character to the left of the image
    char_x = -bbox[0]
    # The y-coordinate centers the character vertically
    char_y = (height - char_height) / 2 - bbox[1]

    draw.text((char_x, char_y), char, font=font, fill=0)

    return image