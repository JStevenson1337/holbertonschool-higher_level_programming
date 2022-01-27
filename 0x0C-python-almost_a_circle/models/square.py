#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """Update Square
        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
        """
        variables = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        if args:
            for i, arg in enumerate(args):
                variables[list(variables.keys())[i]] = arg
        else:
            for key, value in kwargs.items():
                variables[key] = value
        self.id = variables['id']
        self.size = variables['size']
        self.x = variables['x']
        self.y = variables['y']

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

