#!/usr/bin/python3
"""Python Script."""


def inherits_from(obj, a_class):
    """Return True if the object.

    is an instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
