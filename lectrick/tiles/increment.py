from .math_tile import MathTile


class Increment(MathTile):
    TILE_TYPE = "INCREMENT"
    SAMPLE_CHARS = ["↑", "🡑", "⭡", "🠕", "🡩"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles, lambda a: a + 1, self.TILE_TYPE, self.SAMPLE_CHARS)