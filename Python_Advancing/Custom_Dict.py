import json
from pathlib import Path

parent_dict = dict


def get_filepath():
    path = Path(".../data/custom_dict/custom_dict.json").resolve()
    if not path.exists():
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch(exist_ok=True)

    return path


def get_file():
    file_path = get_filepath()

    with file_path.open(mode="r", encoding='utf-8') as file:
        try:
            dictionary = json.load(file)
            return dictionary
        except json.decoder.JSONDecodeError:
            return {}


class CustomDict(parent_dict):
    def __init__(self):
        super(CustomDict, self).__init__()

    def __setitem__(self, key, value):
        file_path = get_filepath()
        dictionary = get_file()

        dictionary.super(CustomDict, self).__setitem__(key, value)

        with file_path.open(mode="w", encoding='utf-8') as file:
            json.dump(dictionary, file, separators=('\n', '='))


if __name__ == '__main__':
    filepath = get_filepath()
    file = get_file()
    print(filepath)
    print(file)
