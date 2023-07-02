#!/usr/bin/python3
"""classes and objects tasks."""


class Square:
    """square class."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise Constructor for Square class.

        Args:
        size (int) : the size of the square. defaults to Zero.
        position (int) : position of a sqaure point. defaults to Zero.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter."""
        return self.__size

    @property
    def position(self):
        """Position getter."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple
           or len(value) != 2
           or type(value[0]) != int
           or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get the area of a square based on a certain size."""
        return self.__size * self.__size

    def my_print(self):
        """Print a squre with #."""
        if self.size == 0:
            print()
            return
        for x in range(self.position[1]):
            print()
        for x in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
