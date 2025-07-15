from PIL import ImageFont

from fontTools.ttLib import TTFont

FONT_FILES = ["fonts/NotoSans-Regular.ttf", "fonts/NotoSansSymbols-Regular.ttf", "fonts/NotoSansSymbols2-Regular.ttf"]
FONT_SIZE = 48

# We map fontTools fonts to PIL fonts
# When the program needs a font, we first check which fontTools font supports the character
# Then, we return the corresponding PIL font

ft_fonts = {}
pil_fonts = {}

for font in FONT_FILES:
    ft_font = TTFont(font)
    ft_fonts[font] = ft_font
    pil_font = ImageFont.truetype(font, FONT_SIZE)
    pil_fonts[font] = pil_font


def get_font_for_character(character):
    for font_name, ft_font in ft_fonts.items():
        if len(character) != 1:
            return ImageFont.load_default()
        if ft_font.getBestCmap().get(ord(character)):
            return pil_fonts[font_name]
    return ImageFont.load_default()
