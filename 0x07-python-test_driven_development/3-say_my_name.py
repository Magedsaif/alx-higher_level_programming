#!/usr/bin/python3
"""A function that prints a message."""


def say_my_name(first_name, last_name=""):
    """Create A function that prints a message.

    Args:
        first_name (str): name to be entered
        last_name (str): name to be entered. Defaults to "".
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
