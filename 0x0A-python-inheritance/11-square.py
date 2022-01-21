#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    Class Square
    """
    def __init__(self, size):
        """
        Constructor
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Area
        """
        return self.__size ** 2

    def __str__(self):
        """
        String
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)