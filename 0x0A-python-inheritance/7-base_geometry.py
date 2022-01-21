#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """A BaseGeometry class """

    def integer_validator(self, name, value):
        """ integer_validator method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif type(value) is int and value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")
