from click import group, option, argument

from .generate_overlays import generate_overlays as generate_overlays_  # To avoid conflict with the option name
from .generate_shapes import generate_shapes as generate_shapes_
from .lookup import lookup_character
from .map_program import map_program
from .reverse_lookup import reverse_lookup as reverse_lookup_
from .run import run_program as run_program_
from .watch import watch


@group()
def lectrick():
    pass


@lectrick.command('lookup')
@argument('character')
@option('--generate-overlays', is_flag=True, help='Generate visual overlays for the character comparison.')
def lookup(character, generate_overlays):
    """Determine what shape this character most closely resembles."""
    results = lookup_character(character, list_strengths=True)
    if results:
        print(f"Best match for '{character}': {results[0][0]} with strength {results[0][1]:.2f}")
        if len(results) > 1:
            print("Other matches:")
            for identifier, strength in results[1:]:
                print(f" - {identifier}: {strength:.2f}")
    else:
        print(f"No matches found for '{character}'.")
    if generate_overlays:
        generate_overlays_(character)


@lectrick.command('reverse-lookup')
@argument('target_shape')
@option('--char-range', default='100', help='Character range to search (e.g., 100, 50-100).')
@option('--min-strength', default=0.0, type=float, help='Minimum strength for a match to be considered.')
def reverse_lookup(target_shape, char_range, min_strength):
    """Find characters that would perform the given action when used."""
    if '-' in char_range:
        char_range = tuple(map(int, char_range.split('-')))
    else:
        char_range = int(char_range)
    for result in reverse_lookup_(target_shape, char_range):
        char, strength = result
        if strength >= min_strength:
            print(f"'{char}' (strength: {strength:.2f})")


@lectrick.command('generate-shapes')
@option('--generate-each-character', is_flag=True, help='Generate individual character images for each shape.')
def generate_shapes(generate_each_character):
    """Generate PNG & SVG files for all shapes in the shapes directory."""
    generate_shapes_(generate_each_character)


@lectrick.command('map')
@argument('program')
@option('--output', default='mapped_program.csv', help='Output file for the mapped program.')
def map_command(program, output):
    """Map a program to its corresponding actions."""
    with open(program, 'r', encoding='utf-8') as f:
        result = map_program(f.read())
    if result:
        with open(output, 'w') as f:
            for line in result:
                f.write(f"{','.join(line)}\n")
        print(f"Mapped program saved to {output}.")
    else:
        print("No actions mapped from the program.")


@lectrick.command('run')
@argument('program')
@option('--visualize', is_flag=True, help='Visualize the program execution.')
@option('--visualize-width', default=10, type=int, help='Width of tile names in visualization.')
@option('--pause', default=0, type=float, help='Pause duration between frames in seconds.')
def run_program(program, visualize, visualize_width, pause):
    """Map a program to its corresponding actions."""
    with open(program, 'r', encoding='utf-8') as f:
        result = f.read()
    if result:
        run_program_(result, visualize=visualize, visualize_width=visualize_width, pause=pause)
        print("Program executed successfully.")


@lectrick.command('chr')
@argument('numeric_value', type=int)
def chr_command(numeric_value):
    """Convert a numeric value to its corresponding character."""
    try:
        character = chr(numeric_value)
        print(f"Character for {numeric_value}: '{character}'")
    except ValueError:
        print(f"Invalid numeric value: {numeric_value}. Must be in the range of valid Unicode code points.")
    except Exception as e:
        print(f"An error occurred: {e}")


@lectrick.command('ord')
@argument('character')
def ord_command(character):
    """Convert a character to its corresponding numeric value."""
    if len(character) != 1:
        print("Please provide a single character.")
        return
    numeric_value = ord(character)
    print(f"Numeric value for '{character}': {numeric_value}")


@lectrick.command('watch')
@argument('file_path')
def watch_command(file_path):
    """Outputs the contents of a file whenever it changes."""
    watch(file_path)


def main():
    lectrick()


if __name__ == '__main__':
    main()
