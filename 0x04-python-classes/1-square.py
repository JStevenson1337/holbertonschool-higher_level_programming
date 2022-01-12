#!/usr/bin/python3
"""A simple Square class that defines a square by its size."""


class Square:
    """A simple Square class that defines a square by its size.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Finds the area of the square.

        Returns:
            int : The area of the square.
        """
        return self.__size ** 2
