from .base import Tile


class PressDetector(Tile):
    TILE_TYPE = "PRESS DETECTOR"
    SAMPLE_CHARS = ["␣"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def start_turn(self, execution_data, *args, **kwargs):
        pressed_key = execution_data.get_pressed_key()
        if pressed_key is not None:
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
                    self.tiles[tile_index].accept_energy(pressed_key, self.x, self.y)
