#!/usr/bin/python3
"""Student Class"""


class Student:
    """Class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return (self.__dict__)
        dictionary = dict()
        for element in attrs:
            for key in self.__dict__:
                if (element == key):
                    dictionary[element] = self.__dict__[key]
        return (dictionary)
