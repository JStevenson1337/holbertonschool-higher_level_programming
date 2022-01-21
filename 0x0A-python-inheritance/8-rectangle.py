#!/usr/bin/python3
""" BaseGeometry class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle Class inherits baseGeometry """
    def __init__(self, width, height):
        """ init method """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
