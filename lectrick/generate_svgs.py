from os import listdir
from os.path import isfile, join
from json import load as json_load

SVG_HEADER = """<svg version="1.1" viewBox="0 0 {} {}" xmlns="http://www.w3.org/2000/svg">"""
SVG_FOOTER = """</svg>"""

DIRECTORY = 'shapes'

def generate_svg_file(source_file):
    with open(source_file, 'r') as file:
        data = json_load(file)
    width = len(data['shape'][0])
    height = len(data['shape'])
    svg_content = SVG_HEADER.format(width, height)
    for y, line in enumerate(data['shape']):
        for x, char in enumerate(line):
            if char == '#':
                svg_content += f'<rect x="{x}" y="{y}" width="1" height="1" fill="black"/>'
            else:
                svg_content += f'<rect x="{x}" y="{y}" width="1" height="1" fill="white"/>'
    svg_content += SVG_FOOTER
    with open(source_file.replace('.json', '.svg'), 'w') as svg_file:
        svg_file.write(svg_content)


def generate_svgs_from_directory(directory):
    json_files = [f for f in listdir(directory) if isfile(join(directory, f)) and f.endswith('.json')]
    for json_file in json_files:
        generate_svg_file(join(directory, json_file))

def generate_svgs():
    generate_svgs_from_directory(DIRECTORY)
    print(f"SVG files generated in the '{DIRECTORY}' directory.")

