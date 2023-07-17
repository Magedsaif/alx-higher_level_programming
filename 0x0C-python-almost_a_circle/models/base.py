#!/usr/bin/python3
"""models/base.py"""
import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns the JSON representation
        of an object (string)"""
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """function that writes an Object to a text file,
        using a JSON representation"""
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for i in list_objs:
                json_dict = cls.to_dictionary(i)
                new_list.append(json_dict)
        js_str = cls.to_json_string(new_list)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(js_str)

    @staticmethod
    def from_json_string(json_string):
        """function that writes an Object to a text file,
        using a JSON representation"""

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
