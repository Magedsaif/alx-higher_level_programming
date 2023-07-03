#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Instantition of object.

        Args:
            __width (int): width of rectangular. Defaults to 0.
            __height (int): height of rectangular. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter.

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter.

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
