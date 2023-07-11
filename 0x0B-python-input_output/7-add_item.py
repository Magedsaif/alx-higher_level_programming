#!/usr/bin/python3
"""Python script."""


import sys
import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding="utf-8") as f:
        # Use the `indent` parameter for pretty-printing.
        return json.dump(my_obj, f)


def load_from_json_file(filename):
    """Create an Object from a “JSON file”."""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)


def add_arguments_to_list(arguments):
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(arguments)
    save_to_json_file(existing_list, 'add_item.json')


if __name__ == '__main__':
    arguments = sys.argv[1:]
    add_arguments_to_list(arguments)
