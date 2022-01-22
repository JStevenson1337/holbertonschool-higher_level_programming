#!/usr/bin/python3
""" Student Class """

Student = __import__('9-student').Student


def to_json(self, attrs=None):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    """
    if type(attrs) is list:
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
    else:
        return self.__dict__
