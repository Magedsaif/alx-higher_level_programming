#!/usr/bin/python3

"""models/Square.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Width."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Width."""
        return self.width

    @size.setter
    def size(self, value):
        """Width."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Width."""
        if args:
            attribute_names = ['id', 'size', 'x', 'y']
            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)
        else:
            for key, value1 in kwargs.items():
                setattr(self, key, value1)

    def __str__(self) -> str:
        """Width."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """Width."""
        dic = dict()
        dic['size'] = self.size
        dic['id'] = self.id
        dic['x'] = self.x
        dic['y'] = self.y
        return (dic)
