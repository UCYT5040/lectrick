from .base import Tile
from ..fire import FireException


class ConditionalHorizontalWire(Tile):
    TILE_TYPE = "CONDITIONAL HORIZONTAL WIRE"
    SAMPLE_CHARS = ["T"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)
        self.pending_vertical_input = None
        self.current_vertical_input = None

    def accept_energy(self, amount, source_x, source_y):
        if source_y == self.y:  # Horizontal input
            if self.pending_input is not None:
                raise FireException(
                    f"FIRE: Tile {self.TILE_TYPE} at {self.x}, {self.y} already has pending input ({self.pending_input}). Source: ({source_x}, {source_y})")
            self.pending_input = (amount, source_x, source_y)
        elif source_x == self.x:  # Vertical input
            if self.pending_vertical_input is not None:
                raise FireException(
                    f"FIRE: Tile {self.TILE_TYPE} at {self.x}, {self.y} already has pending vertical input ({self.pending_vertical_input}). Source: ({source_x}, {source_y})")
            self.pending_vertical_input = (amount, source_x, source_y)

    def advance_turn(self, *args, **kwargs):
        self.current_input = self.pending_input
        self.pending_input = None
        self.current_vertical_input = self.pending_vertical_input
        self.pending_vertical_input = None

    def start_turn(self, *args, **kwargs):
        if self.current_input and self.current_vertical_input:
            vertical_amount = self.current_vertical_input[0]
            if vertical_amount <= 0:
                return
            amount, source_x, source_y = self.current_input
            if source_x < self.x:
                dx = -1
            elif source_x > self.x:
                dx = 1
            else:
                return
            try:
                tile_index = self.tiles.index((self.x - dx, self.y))
            except ValueError:
                return
            self.tiles[tile_index].accept_energy(amount, self.x, self.y)
