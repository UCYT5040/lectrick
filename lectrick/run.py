import sys
from os import system as os_system
from platform import system as platform_system
from time import sleep, time
from typing import Optional

from .map_program import map_program
from .tiles import create_tile

if sys.platform == "win32":
    import msvcrt
else:
    import select
    import sys
    import termios
    import tty

COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"


class ExecutionContext:
    PRESS_TIMEOUT = 0.2  # seconds, estimated keyboard repeat delay

    def __init__(self):
        self.start_time = time()
        self.pressed_key = None
        self.pressed_key_time = None

    @staticmethod
    def _get_pressed_key() -> Optional[int]:
        if sys.platform == "win32":
            if msvcrt.kbhit():
                return ord(msvcrt.getch())
            return None
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
                if rlist:
                    return ord(sys.stdin.read(1))
                return None
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def get_time(self):
        return time() - self.start_time

    def get_pressed_key(self) -> Optional[int]:
        current_key = self._get_pressed_key()
        if current_key is not None:
            if self.pressed_key is None or current_key != self.pressed_key:
                self.pressed_key = current_key
            self.pressed_key_time = time()
        else:
            if self.pressed_key is not None and time() - self.pressed_key_time > self.PRESS_TIMEOUT:
                self.pressed_key = None
                self.pressed_key_time = None
        return self.pressed_key



def clear_screen():
    if platform_system() == "Windows":
        os_system("cls")
    else:
        os_system("clear")


def visualize_tiles(tiles, turn, visualize_width):
    visualization = []
    current_width = 0
    for tile in tiles:
        if tile.x + 1 > current_width:
            current_width = tile.x + 1
            for line in visualization:
                while len(line) < current_width:
                    line.append("")
        while tile.y >= len(visualization):
            visualization.append(["" for _ in range(current_width)])
        tile_visualization = ""
        if tile.current_input:
            tile_visualization += COLOR_YELLOW
        elif tile.pending_input:
            tile_visualization += COLOR_RED
        tile_name = tile.TILE_TYPE[:visualize_width]
        if len(tile_name) < visualize_width:
            tile_name += " " * (visualize_width - len(tile_name))
        tile_visualization += f"{tile_name}"
        tile_visualization += COLOR_RESET
        visualization[tile.y][tile.x] = tile_visualization
    clear_screen()
    print(f"Turn: {turn}")
    for line in visualization:
        print(" | ".join(line))


def execute_frame(tiles, turn, execution_context, visualize, visualize_width):
    for tile in tiles:
        tile.start_turn(execution_context)
    if visualize: visualize_tiles(tiles, turn, visualize_width)
    for tile in tiles:
        tile.end_turn(execution_context)
    if visualize: visualize_tiles(tiles, turn, visualize_width)
    for tile in tiles:
        tile.advance_turn(execution_context)
    if visualize: visualize_tiles(tiles, turn, visualize_width)


def run_program(program, visualize, visualize_width, pause, alternate_engine):
    mapped_program = map_program(program, alternate_engine)
    tiles = []
    for y, row in enumerate(mapped_program):
        for x, tile_type in enumerate(row):
            tiles.append(create_tile(tile_type, x, y, tiles))

    turn = 0
    execution_context = ExecutionContext()

    while True:
        execute_frame(tiles, turn, execution_context, visualize, visualize_width)
        turn += 1
        if pause > 0:
            sleep(pause)
