#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """Read file."""
# Open the text file using "with" statement to ensure it is closed after use.
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
