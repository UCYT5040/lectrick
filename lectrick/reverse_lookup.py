from json import load as json_load
from os import listdir
from os.path import isfile, join
from typing import Union

from char_image import char_image
from compare import compare_character

DIRECTORY = 'shapes'


def reverse_lookup(target_shape: list[str], char_range: Union[tuple[int, int], int] = 100):
    """Find characters that closely resemble a given shape."""
    if isinstance(char_range, int):
        char_min = 0
        char_max = char_range
    elif isinstance(char_range, tuple) and len(char_range) == 2:
        char_min, char_max = char_range
    else:
        raise ValueError("char_range must be an int or a tuple of two ints (min, max).")

    for char_num in range(char_min, char_max + 1):
        char = chr(char_num)
        char_img = char_image(char)

        json_files = [f for f in listdir(DIRECTORY) if isfile(join(DIRECTORY, f)) and f.endswith('.json')]
        max_similarity = -1
        best_match = None

        for json_file in json_files:
            with open(join(DIRECTORY, json_file), 'r') as file:
                data = json_load(file)
            similarity = compare_character(char_img, data['shape'], data.get('bias'))
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = data['identifier']

        if best_match == target_shape:
            yield char, max_similarity
