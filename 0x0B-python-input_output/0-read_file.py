#!/usr/bin/python3
""" Reads a file and prints it to stdout """


def read_file(filename=""):
    """
    read_file:
    Reads a file and prints its content
    """
    with open(filename, 'r') as f:
        print(f.read(), end='')
