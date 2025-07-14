from .base import Tile


class PowerSource(Tile):
    TILE_TYPE = "POWER SOURCE"
    SAMPLE_CHARS = ["🗲", "⚡", "⌁"]
    POWER_LEVEL = 255

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)
        self.has_sent_power = False

    def start_turn(self):
        if not self.has_sent_power:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    target_x = self.x + dx
                    target_y = self.y + dy
                    try:
                        tile_index = self.tiles.index((target_x, target_y))
                    except ValueError:
                        continue
                    self.tiles[tile_index].accept_energy(self.POWER_LEVEL, self.x, self.y)
            self.has_sent_power = True
