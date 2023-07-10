#!/usr/bin/python3
"""Python Script."""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """Area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator.

        Args:
            name (str): str
            value (int): int
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
