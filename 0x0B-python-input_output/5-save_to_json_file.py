#!/usr/bin/python3
"""Python script."""

import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding="utf-8") as f:
        # Use the `indent` parameter for pretty-printing.
        return json.dump(my_obj, f)
