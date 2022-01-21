#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size):
        """
        Constructor
        """
        if self.integer_validator("size", size):
            self.__size = size
            super().__init__(size, size)

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
