from lookup import lookup_character
from regex import findall

def map_program(program: str) -> list[list[str]]:
    for line in program.splitlines():
        graphemes = findall(r"\X", line)
        for char in graphemes:
            print(char, lookup_character(char))
    return [
        [
            lookup_character(char) for char in findall(r"\X", line)
        ]
        for line in program.splitlines()
    ]
