#!/usr/bin/python3
""" Lookup class """


def lookup(obj):
    """ Get attribute and methods from an object

        Args:
            obj: object to get attributes and methods from

        Returns:
            list[str]: list of attributes and methods
    """
    return dir(obj)
