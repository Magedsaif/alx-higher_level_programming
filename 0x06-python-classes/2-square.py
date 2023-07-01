#!/usr/bin/python3
"""
classes and objects tasks
"""


class Square:
    """
    square class
    """
    def __init__(self, size=0):
        """
        the constructor for Square class
        Args:
        size (int) : the size of the square. defaults to Zero.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
