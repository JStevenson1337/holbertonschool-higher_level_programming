#!/usr/bin/python3
""" Write a function that prints a square with the character """


def print_square(size):
    """ Prints a square with the character #
    Args:
        size (int): size of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    octothorpe = "#"
    i = 0
    j = 0
    if size <= 0.0 and type(size) == float:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    while i < size:
        while j < size:
            print(octothorpe, end="")
            j += 1
        print("")
        i += 1
        j = 0
