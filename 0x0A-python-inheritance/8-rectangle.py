#!/usr/bin/python
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
    try:
        if type(value) is not int:


class Rectangle(BaseGeometry):
    """ A Retangle Class inherits baseGeometry """
    def __init__(self, width, height):
        self.width = width
        self.height = height

