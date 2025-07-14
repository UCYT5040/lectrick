from regex import findall

from .lookup import lookup_character


def map_program(program: str) -> list[list[str]]:
    return [
        [
            lookup_character(char) for char in findall(r"\X", line)
        ]
        for line in program.splitlines()
    ]
