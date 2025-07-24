from .math_tile import MathTile


class Split(MathTile):
    TILE_TYPE = "SPLIT"
    SAMPLE_CHARS = ["÷"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles, lambda a: a // 2, self.TILE_TYPE, self.SAMPLE_CHARS)
