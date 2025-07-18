from .one_way_base import OneWayTile


class Not(OneWayTile):
    TILE_TYPE = "NOT"
    SAMPLE_CHARS = ["≠", "≄", "≉"]
    POWER = 255

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def acceptance_filter(self, source_x, source_y):
        if source_y != self.y:
            return False
        return True

    def start_turn(self, *args, **kwargs):
        if not self.current_input:
            amount = 0
        else:
            amount = self.current_input[0]
        if amount > 0:
            amount = 0
        else:
            amount = self.POWER
        if amount == 0:
            return
        for dx in (-1, 1):
            try:
                tile_index = self.tiles.index((self.x - dx, self.y))
            except ValueError:
                return
            self.tiles[tile_index].accept_energy(amount, self.x, self.y)
