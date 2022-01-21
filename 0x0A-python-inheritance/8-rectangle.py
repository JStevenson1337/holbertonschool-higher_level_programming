#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """A BaseGeometry class

        Attributes:
    """
    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif type(value) is int and value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value


class Rectangle(BaseGeometry):
    """ A Retangle Class inherits baseGeometry """
    def __init__(self, width, height):
        """ init method """
        self.__width = integer_validator("width", width)
        self.__height = integer_validator("height", height)
        self.__height = height
        self.width = width
