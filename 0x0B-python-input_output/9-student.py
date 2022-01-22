#!/usr/bin/python3
""" A Student Class """


class Student:
    """ A Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initialize the Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if type(attrs) is list:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__
