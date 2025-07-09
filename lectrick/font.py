from PIL import ImageFont

FONTS = [
    "C:/Windows/Fonts/consola.ttf",
    "/System/Library/Fonts/Menlo.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
]

font = None


def get_font(font_index):
    try:
        return ImageFont.truetype(FONTS[font_index], 16)
    except IOError:
        return None


i = 0
while font is None and i < len(FONTS):
    font = get_font(i)
    i += 1

if font is None:
    font = ImageFont.load_default()
    print("Warning: No suitable font found, using default font. This font is non-monospaced and may work unexpectedly.")
