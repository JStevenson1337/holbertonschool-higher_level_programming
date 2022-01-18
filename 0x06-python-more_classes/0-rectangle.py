#!/usr/bin/python3
""" A class Rectangle that defines a rectangle """


class Rectangle:
    """ Class Rectangle
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Finds the width of the rectangle
        Returns:
            width (int): width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Finds the height of the rectangle
        Returns:
            height of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle
        Args:
            value (int): width of
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle
                Args:
                    value (int -> optional): height of
                """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
