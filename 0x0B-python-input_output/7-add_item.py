#!/usr/bin/python3
"""load_from_json_file function"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    list_argv = []
    for arg in sys.argv[1:]:
        list_argv.append(arg)

    name = 'add_item.json'

    if not os.path.exists(name):
        with open(name, 'w') as file:
            file.write("[]")

    existing_data = load_from_json_file(name)
    existing_data.extend(list_argv)

    save_to_json_file(existing_data, name)

    load_from_json_file(name)


if __name__ == "__main__":
    main()
