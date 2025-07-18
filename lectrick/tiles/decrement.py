from .one_way_base import OneWayTile


class Decrement(OneWayTile):
    TILE_TYPE = "DECREMENT"
    SAMPLE_CHARS = ["↓", "⇩", "🡓", "⭣", "🠗", "🡫"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def start_turn(self, *args, **kwargs):
        if not self.current_input:
            return
        amount, source_x, source_y = self.current_input
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
                self.tiles[tile_index].accept_energy((amount-1) % 256, self.x, self.y)
