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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get the area of a square based on a certain size."""
        return self.__size * self.__size
