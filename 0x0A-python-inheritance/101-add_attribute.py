#!/usr/bin/python3
"""Python Script."""


def add_attribute(obj, attribute, value):
    """Add attribute to object if possible."""
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
