#!/usr/bin/python3
"""Python script."""


def append_write(filename="", text=""):
    """Append write."""
    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
