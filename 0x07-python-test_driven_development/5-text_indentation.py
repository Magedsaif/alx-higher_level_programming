#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters:., ? and:."""


def text_indentation(text):
    """Print text with 2 new lines.

    Args:
        text (st): text given

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in ":.?":
        text = text.replace(character, character + "\n\n")

    list_lines = []
    splitted_text = text.split('\n')
    for line in splitted_text:
        stripped_line = line.strip(' ')
        list_lines.append(stripped_line)

    revised_lines = "\n".join(list_lines)

    print(revised_lines, end="")
