#!/usr/bin/python3
""" Write a function that prints a square with the character """
    
    
def print_square(size):
    """[summary]

    Args:
        size ([type]): [description]
    """
    octothorpe = "#"
    i = 0
    j = 0
    while i < size:
        while j < size:
            print(octothorpe, end="")
            j += 1
        print("")
        i += 1
        j = 0   
    














# Write a function that prints a square with the character #.

# Prototype: def print_square(size):
# size is the size length of the square
# size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
# You are not allowed to import any module
