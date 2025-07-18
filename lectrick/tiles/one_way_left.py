from .base import Tile


class OneWayLeftTile(Tile):
    TILE_TYPE = "ONE WAY LEFT"
    SAMPLE_CHARS = ["<"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def accept_energy(self, amount, source_x, source_y):
        if source_y != self.y:
            return
        if source_x < self.x:  # The energy is coming from the left
            return
        self.pending_input = amount

    def advance_turn(self, *args, **kwargs):
        self.current_input = self.pending_input
        self.pending_input = None

    def start_turn(self, *args, **kwargs):
        if not self.current_input:
            return
        amount = self.current_input
        if amount <= 0:
            return
        # Send energy to the left
        target_x = self.x - 1
        target_y = self.y
        try:
            tile_index = self.tiles.index((target_x, target_y))
        except ValueError:
            return
        self.tiles[tile_index].accept_energy(amount, self.x, self.y)
