#!/usr/bin/python3
""" "returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """ Get attribute and methods from an object

        Args:
            obj: object to get attributes and methods from

        Returns:
            list[str]: list of attributes and methods
    """
    for i in dir(obj):
        print(i, end="\n")
    return dir(obj)

