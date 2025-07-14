from os import system as os_system
from platform import system as platform_system
from time import sleep

from .map_program import map_program
from .tiles import create_tile

COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"


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
        if tile.y >= len(visualization):
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


def execute_frame(tiles, turn, visualize, visualize_width):
    for tile in tiles:
        tile.start_turn()
    if visualize: visualize_tiles(tiles, turn, visualize_width)
    for tile in tiles:
        tile.end_turn()
    if visualize: visualize_tiles(tiles, turn, visualize_width)
    for tile in tiles:
        tile.advance_turn()
    if visualize: visualize_tiles(tiles, turn, visualize_width)


def run_program(program, visualize, visualize_width, pause):
    mapped_program = map_program(program)
    tiles = []
    for y, row in enumerate(mapped_program):
        for x, tile_type in enumerate(row):
            tiles.append(create_tile(tile_type, x, y, tiles))

    turn = 0
    while True:
        execute_frame(tiles, turn, visualize, visualize_width)
        turn += 1
        if pause > 0:
            sleep(pause)
