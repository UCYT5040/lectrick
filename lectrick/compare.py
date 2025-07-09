from PIL import Image


def compare_character(char: Image, shape: list[str], bias: float = 0.0) -> float:
    if bias is None: bias = 0.0  # Bias is usually provided from dict.get(), which returns None, so check for that

    width = len(shape[0])
    height = len(shape)

    char = char.resize((width * 2, height * 2))

    char_data = char.load()

    similarity = 0

    for y in range(height):
        for x in range(width):
            pixel_data = 255 * 4
            for dy in range(2):
                for dx in range(2):
                    pixel_data -= char_data[x * 2 + dx, y * 2 + dy]
            if pixel_data >= 255 and shape[y][x] == '#':
                similarity += pixel_data
            elif pixel_data < 255 and shape[y][x] == ' ':
                similarity += 1
            elif pixel_data < 255 and shape[y][x] == '#':
                similarity -= pixel_data  # Penalty for mismatches

    final_similarity = similarity / (width * height * 128) + bias

    return final_similarity if final_similarity > 0 else 0.0
