#!/usr/bin/python3
"""Function that returns the list of attributes.

and methods of an object.
"""


def lookup(obj):
    """Return list of Att and methods.

    Args:
        obj (object): object
    """
    return dir(obj)
