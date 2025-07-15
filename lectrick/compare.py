from PIL import Image, ImageDraw
from numpy import array as np_array, float64 as np_float64
from skimage.metrics import structural_similarity as ssim

from .crop_image import crop_image
from .font import get_font_for_character

def compare_character(char: str, shape_name: str) -> float:
    try:
        shape_path = f"shapes/{shape_name}.png"
        shape_image = Image.open(shape_path).convert('L')
    except FileNotFoundError:
        return 0.0

    font = get_font_for_character(char)
    bbox = font.getbbox(char)

    if not (bbox and bbox[2] > bbox[0] and bbox[3] > bbox[1]):
        return 0.0

    char_width, char_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    char_image = Image.new('L', (char_width, char_height), 255)
    draw = ImageDraw.Draw(char_image)
    draw.text((-bbox[0], -bbox[1]), char, font=font, fill=0)

    char_image = crop_image(char_image)

    char_image = char_image.resize(shape_image.size, Image.Resampling.LANCZOS)

    shape_array = np_array(shape_image, dtype=np_float64)
    char_array = np_array(char_image, dtype=np_float64)

    # get similarity
    try:
        score = ssim(shape_array, char_array, data_range=255)
    except Exception:
        return 0.0

    similarity = max(0.0, score)
    
    return similarity