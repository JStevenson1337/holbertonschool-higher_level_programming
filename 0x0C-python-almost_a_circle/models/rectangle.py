#!/usr/bin/python3
""" Rectangle """
from models.base import Base
import json


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle"""
        self.width = self.hw_validator("width", width)
        self.height = self.hw_validator("height", height)
        self.x = self.xy_validator("x", x)
        self.y = self.xy_validator("y", y)
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x setter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x >= 0:
            self.__x = x
            return
        raise ValueError("x must be >= 0")

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y >= 0:
            self.__y = y
            return
        raise ValueError("y must be >= 0")

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        """ Update attributes of Rectangle """
        if args:
            arg_dict = {'id': args[0], 'width': args[1], 'height': args[2],
                        'x': args[3], 'y': args[4]}
            for key, value in arg_dict.items():
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def __str__(self):
        """Return string representation of Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def hw_validator(self, name, value):
        """
        Raises: TypeError if Value is not int
                ValueError if value <=0
        """
        if type(value) is int:
            if value < 1:
                raise ValueError("{:s} must be > 0".format(name))
            return value
        raise TypeError("{:s} must be an integer".format(name))

    def xy_validator(self, name, value):
        """
        Raises: TypeError if Value is not int
                ValueError if value <=0
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("{:s} must be >= 0".format(name))
            return value
        raise TypeError("{:s} must be an integer".format(name))
