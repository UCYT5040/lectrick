from .one_way_base import OneWayTile


class LightBlock(OneWayTile):
    TILE_TYPE = "LIGHT BLOCK"
    SAMPLE_CHARS = ["⬛", "⯀", "◼", "▮"]

    def __init__(self, x, y, tiles):
        super().__init__(x, y, tiles)

    def start_turn(self):
        pass

    def end_turn(self):
        if self.current_input:
            amount, source_x, source_y = self.current_input
            print(chr(amount), end="", flush=True)
