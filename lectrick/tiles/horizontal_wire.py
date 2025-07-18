from .one_way_base import OneWayTile


class HorizontalWire(OneWayTile):
    TILE_TYPE = "HORIZONTAL WIRE"
    SAMPLE_CHARS = ["-", "‐", "‒"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def acceptance_filter(self, source_x, source_y):
        if source_y != self.y:
            return False
        return True

    def start_turn(self, *args, **kwargs):
        if self.current_input:
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
