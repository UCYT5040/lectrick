from click import group, option, argument

from .generate_overlays import generate_overlays as generate_overlays_  # To avoid conflict with the option name
from .generate_shapes import generate_shapes as generate_shapes_
from .lookup import lookup_character
from .map_program import map_program
from .reverse_lookup import reverse_lookup as reverse_lookup_
from .run import run_program as run_program_


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

if __name__ == '__main__':
    lectrick()
