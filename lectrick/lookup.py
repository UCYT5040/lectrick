from .compare import compare_character
from .tiles import list_tile_types

DIRECTORY = 'shapes'


def lookup_character(character, list_strengths=False):
    results = []

    for tile in list_tile_types():
        similarity = compare_character(character, tile)
        results.append((tile, similarity))

    results.sort(key=lambda x: x[1], reverse=True)

    if list_strengths:
        return results
    else:
        return results[0][0] if results else None
