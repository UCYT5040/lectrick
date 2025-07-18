from regex import findall

from .lookup import lookup_character


def map_program(program: str, alternate_engine) -> list[list[str]]:
    return [
        [
            lookup_character(char, alternate_engine=alternate_engine) for char in findall(r"\X", line)
        ]
        for line in program.splitlines()
    ]
