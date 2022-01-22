#!/usr/bin/python3
""" Student Class """

Student = __import__('9-student').Student


def to_json(self, attrs=None):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    """
    if attrs is None:
        return self.__dict__
    else:
        return {key: value for key, value in self.__dict__.items() if key in attrs}
