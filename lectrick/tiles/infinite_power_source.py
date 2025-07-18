from .base import Tile


class InfinitePowerSource(Tile):
    TILE_TYPE = "INFINITE POWER SOURCE"
    SAMPLE_CHARS = ["⏻"]
    POWER_LEVEL = 255

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def start_turn(self, *args, **kwargs):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx == 0 and dy == 0) or (dx != 0 and dy != 0):
                    continue
                target_x = self.x + dx
                target_y = self.y + dy
                try:
                    tile_index = self.tiles.index((target_x, target_y))
                except ValueError:
                    continue
                self.tiles[tile_index].accept_energy(self.POWER_LEVEL, self.x, self.y)
