#!/usr/bin/python
""" BaseGeometry class """


class BaseGeometry:
    """A BaseGeometry class

    Attributes:
    """

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


