from .one_way_base import OneWayTile


class VerticalWire(OneWayTile):
    TILE_TYPE = "VERTICAL WIRE"
    SAMPLE_CHARS = ["|"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def acceptance_filter(self, source_x, source_y):
        if source_x != self.x:
            return False
        return True

    def start_turn(self):
        if self.current_input:
            amount, source_x, source_y = self.current_input
            if source_y < self.y:
                dy = -1
            elif source_y > self.y:
                dy = 1
            else:
                return
            try:
                tile_index = self.tiles.index((self.x, self.y - dy))
            except ValueError:
                return
            self.tiles[tile_index].accept_energy(amount, self.x, self.y)
