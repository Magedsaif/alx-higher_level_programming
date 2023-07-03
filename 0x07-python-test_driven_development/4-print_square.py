#!/usr/bin/python3
"""A function that prints a square with the character #."""

def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): size of a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size:
        for x in range(size):
            print("#" * size, end=" ")
            print()
    else:
        print()
