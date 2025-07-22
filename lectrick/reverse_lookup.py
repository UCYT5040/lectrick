from typing import Union, Tuple, List, TypeAlias, Literal

from .compare import compare_character
from .tiles import list_tile_types

DIRECTORY = 'shapes'

# Cannot use `type` alias statement on Python 3.11 (syntax was added in Python 3.12)
# type CharRangePart = Union[tuple[int, int], int]
# type CharRange = Union[list[CharRangePart], CharRangePart, "clean"]

CharRangePart: TypeAlias = Union[Tuple[int, int], int]
CharRange: TypeAlias = Union[List[CharRangePart], CharRangePart, Literal["clean"]]

CHAR_RANGES = {  # Do not include invisible characters (but may include unassigned characters)
    "clean": [
        (32, 126),  # Basic Latin
        (160, 191),  # Latin-1 Punctuation & Symbols (but not letters)
        (215, 215),  # Latin-1 Multiplication Sign
        (247, 247),  # Latin-1 Division Sign
        (448, 451),  # African clicks, which look more like symbols than letters
        (8211, 8266),  # Unicode symbols
        # The next few ranges are from General Punctuation, with non-visible characters removed
        (8208, 8208),  # Hyphen
        (8210, 8231),
        (8240, 8286),
        # End of General Punctuation
        (8287, 9210),  # Many symbols
        (9312, 9727),  # Many symbols
        (9728, 10175),  # Many symbols
        (119040, 119272),  # Western Musical Symbols
        (128768, 128883),  # Alchemical Symbols
        (126976, 127221),  # Game Symbols
    ]
}


def reverse_lookup(target_shape: list[str], char_range: CharRange = 100):
    """Find characters that closely resemble a given shape."""
    if isinstance(char_range, int) or isinstance(char_range, tuple):
        char_range = [char_range]
    elif char_range in CHAR_RANGES:
        char_range = CHAR_RANGES[char_range]
    elif not isinstance(char_range, list):
        raise ValueError(
            "char_range must be an int, a tuple of two ints, a list of such parts, or a predefined range name (like 'clean').")

    for char_range_part in char_range:
        if isinstance(char_range_part, int):
            char_min = 0
            char_max = char_range_part
        elif isinstance(char_range_part, tuple) and len(char_range_part) == 2:
            char_min, char_max = char_range_part
        else:
            raise ValueError("Each part of char_range must be an int or a tuple of two ints (min, max).")
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
