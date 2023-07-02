#!/usr/bin/python3
"""classes and objects tasks."""


class Square:
    """square class."""

    def __init__(self, size=0):
        """
        Initialise Constructor for Square class.

        Args:
        size (int) : the size of the square. defaults to Zero.
        """
        self.__size = size

    @property
    def size(self):
        """Size getter."""
        return self.__size

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
        if self.size:
            for x in range(self.size):
                print("#" * self.size, end='')
                print()
        else:
            print()
