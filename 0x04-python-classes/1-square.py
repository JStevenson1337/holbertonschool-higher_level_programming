#!/usr/bin/python3
"A simple Square class that defines a square by its size."


TypeError = "size must be an integer"
ValueError = "size must be >= 0"

class Square:
    "A simple Square class that defines a square by its size."
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size

    def area(self):
        return self.__size ** 2
