#!/usr/bin/python3
"""Write file."""


def write_file(filename="", text=""):
    """Write file."""
# Open the text file using "with" statement to ensure it is closed after use.
    with open(filename, mode='w', encoding='utf-8') as f:
        return (f.write(text))
