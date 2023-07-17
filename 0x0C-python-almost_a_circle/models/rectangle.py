#!/usr/bin/python3
"""models/rectangle.py"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Width."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Width."""
        return self.__height

    @height.setter
    def height(self, value):
        """Width."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Width."""
        return self.__x

    @x.setter
    def x(self, value):
        """Width."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Width."""
        return self.__y

    @y.setter
    def y(self, value):
        """Width."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Width."""
        return self.__width * self.__height

    def display(self):
        """Width."""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """Width."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Width."""
        if args:
            attribute_names = ['id', 'width', 'height', 'x', 'y']
            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)
        else:
            for key, value1 in kwargs.items():
                setattr(self, key, value1)

    def to_dictionary(self):
        """Width."""
        dic = dict()
        dic['width'] = self.width
        dic['height'] = self.height
        dic['id'] = self.id
        dic['x'] = self.x
        dic['y'] = self.y
        return (dic)
