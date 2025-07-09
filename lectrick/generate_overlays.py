# generate_overlays.py
from json import load as json_load
from os import listdir
from os.path import isfile, join

from PIL import Image

from char_image import char_image

from unicodedata import name as unicode_name

DIRECTORY = 'shapes'
OVERLAY_DIRECTORY = 'overlays'


def generate_overlays(char):
    print("Red: Expected to be empty space")
    print("Green: Expected to be filled space")
    print("Blue: Actual pixel data")
    print("Blue-Red (purple): Pixel data is there, but unexpected")
    print("Blue-Green (cyan): Pixel data is present, and is expected")
    char_file_safe = char
    char_img = char_image(char)
    try:
        char_img.save(join(OVERLAY_DIRECTORY, f"ORIGINAL_{char_file_safe}.png"))
    except OSError:
        char_file_safe = unicode_name(char, f"U+{ord(char):04X}").lower().replace(' ', '_')
        char_img.save(join(OVERLAY_DIRECTORY, f"ORIGINAL_{char_file_safe}.png"))
    json_files = [f for f in listdir(DIRECTORY) if isfile(join(DIRECTORY, f)) and f.endswith('.json')]

    for json_file in json_files:
        with open(join(DIRECTORY, json_file), 'r') as file:
            data = json_load(file)
        shape = data['shape']
        width = len(shape[0])
        height = len(shape)
        char_img_resized = char_img.resize((width * 2, height * 2))
        char_img_resized.save(join(OVERLAY_DIRECTORY, f"RESIZED_{data['identifier']}_{char_file_safe}.png"))
        overlay_data = char_img_resized.load()
        overlay_img = Image.new('RGB', (width * 2, height * 2), (255, 255, 255))
        for y in range(height):
            for x in range(width):
                rgb = [0, 0, 0]
                if shape[y][x] == '#':
                    rgb[1] = 255
                else:
                    rgb[0] = 255
                for dy in range(2):
                    for dx in range(2):
                        pixel_rgb = rgb.copy()
                        pixel_data = overlay_data[x * 2 + dx, y * 2 + dy]
                        if pixel_data < 128:
                            pixel_rgb[2] = 255
                        overlay_img.putpixel((x * 2 + dx, y * 2 + dy), tuple(pixel_rgb))
        overlay_img.save(join(OVERLAY_DIRECTORY, f"{data['identifier']}_{char_file_safe}.png"))
