#!/usr/bin/python3
""" Reads a file and prints it to stdout """


def read_file(filename=""):
    """
    read_file:
    Reads a file and prints its content
    """
    try:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    finally:
        f.close()
