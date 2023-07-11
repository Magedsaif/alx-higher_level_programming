#!/usr/bin/python3
"""Python script."""


class Student:
    """Student."""

    def __init__(self, first_name, last_name, age):
        """Student.

        Args:
            first_name (str): first_name
            last_name (str): last_name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def to_json(self):
        """To_json."""
        return self.__dict__
