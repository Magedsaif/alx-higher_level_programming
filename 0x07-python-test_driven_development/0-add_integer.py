#!/usr/bin/python3
"""Add two integar."""


def add_integer(a, b=98):
    """
    Add two integars.

    Args:
        a (int): number to be added
        b (int): number to be added. Defaults to 98.

    Returns:
        int: sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + (b)
