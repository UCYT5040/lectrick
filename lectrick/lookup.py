from json import load as json_load
from os import listdir
from os.path import isfile, join

from char_image import char_image
from compare import compare_character

DIRECTORY = 'shapes'


def lookup_character(character, list_strengths=False):
    char_img = char_image(character)
    results = []
    json_files = [f for f in listdir(DIRECTORY) if isfile(join(DIRECTORY, f)) and f.endswith('.json')]

    for json_file in json_files:
        with open(join(DIRECTORY, json_file), 'r') as file:
            data = json_load(file)
        shape = data['shape']
        similarity = compare_character(char_img, shape, data.get('bias'))
        results.append((data['identifier'], similarity))

    results.sort(key=lambda x: x[1], reverse=True)

    if list_strengths:
        return results
    else:
        return results[0][0] if results else None
