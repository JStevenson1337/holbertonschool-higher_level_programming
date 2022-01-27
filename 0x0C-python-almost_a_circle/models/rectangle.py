#!/usr/bin/python3
""" Rectangle """
from models.base import Base
import json


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        ("Instantiation method\n"
         "    Args:\n"
         "        width: width of the rectangle\n"
         "        height: height of the rectangle\n"
         "        x: x position of the rectangle\n"
         "        y: y position of the rectangle\n"
         "        id: id of the rectangle\n"
         "    ")
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) == int:
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = width
            return
        raise TypeError("width must be an integer")

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) == int:
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height
            return
        raise TypeError("height must be an integer")

    @property
    def x(self):
        """x setter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the rectangle's Area"""
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        idd = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(idd, x, y, w, h)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        set_args = dict(id=self.id, width=self.width, height=self.height, x=self.x, y=self.y)
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                set_args[list(set_args.keys())[i]] = arg
        else:
            for key, value in kwargs.items():
                set_args[key] = value
        self.id = set_args['id']
        self.width = set_args['width']
        self.height = set_args['height']
        self.x = set_args['x']
        self.y = set_args['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        print_dict_rectangle = {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
        return dict(print_dict_rectangle)


