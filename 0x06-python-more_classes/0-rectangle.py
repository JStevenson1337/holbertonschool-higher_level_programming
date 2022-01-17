#!/usr/bin/python3
""" A Rectangle Class """


class Rectangle:
    """
        Initializes the rectangle.
        `width` and `height` must be integers and >= 0.
        `pep8` recommends to use `self.__width` instead of `self.width`.
        Returns:
            None
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        if self.width is not (type(int)):
            raise TypeError("width must be an integer")
        elif self.width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width

    @property
    def height(self):
        if self.height is not (type(int)):
            raise TypeError("height must be an integer")
        elif self.height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height
