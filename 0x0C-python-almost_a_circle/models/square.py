#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square
        Args:
            size: size of Square
            x: x coordinate of Square
            y: y coordinate of Square
            id: id of Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.width, self.x, self.y)

    def update(self, *args, **kwargs):
        """Update Square
        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
        """
        if args:
            update_dict = {'id': args[0], 'size': args[1], 'x': args[2],
                           'y': args[3]}
        else:
            update_dict = kwargs
        for key, value in update_dict.items():
            if key == 'id':
                self.id = value
            if key == 'size':
                self.size = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
