#!/usr/bin/python3
"""Python Script."""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified class.

    Args:
        obj (object): object
        a_class (class): class
    """
    return type(obj) == a_class
