# !/usr/bin/python3
""" Base class for all models """
import json


class Base:
    """ Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation method
        Args:
            id: id of the instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a json string
        Args:
            list_dictionaries: list of dictionaries
        Returns:
            json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file
        Args:
            list_objs: list of instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                f.write(cls.to_json_string([cls.to_dictionary(obj)
                                            for obj in list_objs]))


