#!/usr/bin/python3
""" Reads a file and prints it to stdout """


def read_file(filename=""):
    """
    read_file:
    Reads a file and prints its content
    """
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        raise FileNotFoundError("No such file: " + filename)
    finally:
        f.close()

