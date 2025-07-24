from .one_way_base import OneWayTile

# This class is a base for all mathematical tiles.
# It allows you to define tiles that perform math operations (like increment, decrement, double, etc.)
# by passing a function for the operation, along with the tile type and sample characters.

class MathTile(OneWayTile):
    def __init__(self, x, y, tiles, operation, tile_type, sample_chars):
        super().__init__(x, y, tiles)
        self.operation = operation
        self.TILE_TYPE = tile_type
        self.SAMPLE_CHARS = sample_chars
        
    def start_turn(self, *args, **kwargs):
        if not self.current_input:
            return
        amount, source_x, source_y = self.current_input
        result = self.operation(amount) % 256
        acceptance_dx = -1 if source_x < self.x else 1 if source_x > self.x else 0
        acceptance_dy = -1 if source_y < self.y else 1 if source_y > self.y else 0

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx == 0 and dy == 0) or (dx == acceptance_dx and dy == acceptance_dy) or (abs(dx) + abs(dy) > 1):
                    continue
                target_x = self.x + dx
                target_y = self.y + dy
                try:
                    tile_index = self.tiles.index((target_x, target_y))
                except ValueError:
                    continue
                self.tiles[tile_index].accept_energy(result, self.x, self.y)