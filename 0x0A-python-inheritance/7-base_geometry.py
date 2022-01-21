#!/usr/bin/python
""" BaseGeometry class """


def integer_validator(name, value):
    """ integer_validator method

    Args:
        name: name of the value
        value: value to validate
    """
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0 or type(value) is not int:
        raise ValueError("{} must be greater than 0".format(name))


class BaseGeometry:
    """A BaseGeometry class

    Attributes:
    """

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")
