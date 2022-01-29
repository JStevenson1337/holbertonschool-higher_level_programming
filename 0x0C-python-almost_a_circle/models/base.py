#!/usr/bin/python3
""" Base class for all models """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation method
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
        """ Return the JSON string representation of list_dictionaries
        Args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        j_object = []
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                j_object = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(j_object))

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of the JSON string representation json_string
        Args:
            json_string: string
        """
        if json_string is None or len(json_string) <= 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes already set
        Args:
            dictionary: dictionary of attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                listd = cls.from_json_string(file.read())
                return [cls.create(**i) for i in listd]
        except Exception:
            return []
