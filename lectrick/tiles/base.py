class Tile:
    TILE_TYPE = ""
    SAMPLE_CHARS = []

    def __init__(self, x, y, tiles):
        self.x = x
        self.y = y
        self.tiles = tiles
        self.pending_input = None
        self.current_input = None

    def __repr__(self):
        return f"Tile(x={self.x}, y={self.y}, type={self.TILE_TYPE})"

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.x == other.x and self.y == other.y and self.TILE_TYPE == other.TILE_TYPE
        if isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented

    def accept_energy(self, amount, source_x, source_y):
        pass  # To be implemented in subclasses

    def start_turn(self, *args, **kwargs):
        pass  # To be implemented in subclasses

    def end_turn(self, *args, **kwargs):
        pass  # To be implemented in subclasses

    def advance_turn(self, *args, **kwargs):
        pass  # To be implemented in subclasses
