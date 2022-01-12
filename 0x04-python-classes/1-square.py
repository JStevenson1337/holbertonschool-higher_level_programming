#!/usr/bin/python3
"A simple Square class that defines a square by its size."


class Square:
    "A simple Square class that defines a square by its size."
    def __init__(self, size=0):
        TypeError = "size must be an integer"
        ValueError = "size must be >= 0"
        if type(size) != int:
            raise TypeError
        elif size < 0:
            raise ValueError
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
