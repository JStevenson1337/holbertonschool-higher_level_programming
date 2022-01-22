#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """
    Args:
        obj: object to convert to JSON
    Return:
        JSON representation of object
    """
    return obj.__dict__
