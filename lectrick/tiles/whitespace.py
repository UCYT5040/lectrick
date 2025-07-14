from .base import Tile


class Whitespace(Tile):
    TILE_TYPE = "WHITESPACE"
    SAMPLE_CHARS = [" "]  # No need to add more whitespace characters, as they are automatically cropped down to 0x0

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)
