from .base import Tile


class Clock(Tile):
    TILE_TYPE = "CLOCK"
    SAMPLE_CHARS = [
        "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛",
        "🕜", "🕝", "🕞", "🕟", "🕠", "🕡", "🕢", "🕣", "🕤", "🕥", "🕦", "🕧"
    ]
    POWER = 255

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)
        self.last_time = None

    def start_turn(self, execution_data, *args, **kwargs):
        current_time = execution_data.get_time()
        if not self.last_time:
            self.last_time = current_time
            return
        if current_time - self.last_time >= 1:
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
                    self.tiles[tile_index].accept_energy(255, self.x, self.y)
            self.last_time = current_time
