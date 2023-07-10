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


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from the base geometry class."""

    # constructor method to initialize instance variables of rectangle object
    def __init__(self, width, height):
        """Validate and initialize width and height.

        Args:
            width (int): width
            height (int): height
        """
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """Calculate Area."""
        return self.__width * self.__height

    def __str__(self):
        """Return string."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
