# !/usr/bin/python3
""" Base class for all models """
from typing import List


class Base:
    """ Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation method
        Args:
            id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
