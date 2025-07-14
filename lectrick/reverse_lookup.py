from typing import Union

from .compare import compare_character
from .tiles import list_tile_types

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

        max_similarity = -1
        best_match = None

        for tile in list_tile_types():
            similarity = compare_character(char, tile)
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = tile

        if best_match == target_shape:
            yield char, max_similarity
