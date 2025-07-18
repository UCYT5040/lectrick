from lectrick.fire import FireException
from .base import Tile


# One-way meaning it can only accept energy from one direction, and starts a fire if it receives energy from any other
# direction.
# Not to be confused with one-way wires (left or right) that allow energy to pass through in one direction only, and
# simply ignore energy from the other direction (does not start a fire).

class OneWayTile(Tile):
    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def acceptance_filter(self, source_x, source_y):
        return True  # Override this method in subclasses to implement specific acceptance logic

    def accept_energy(self, amount, source_x, source_y):
        if not self.acceptance_filter(source_x, source_y):
            return
        if self.pending_input is not None:
            raise FireException(
                f"FIRE: Tile {self.TILE_TYPE} at {self.x}, {self.y} already has pending input ({self.pending_input}). Source: ({source_x}, {source_y})")
        self.pending_input = (amount, source_x, source_y)

    def advance_turn(self, *args, **kwargs):
        self.current_input = self.pending_input
        self.pending_input = None
