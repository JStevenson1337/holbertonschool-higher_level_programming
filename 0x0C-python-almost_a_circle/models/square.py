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
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.width, self.x, self.y)

    def update(self, *args, **kwargs):
        """Update Square attributes"""
        if args:
            arg_dict = {'id': args[0], 'size': args[1], 'x': args[2],
                        'y': args[3]}
            for key, value in arg_dict.items():
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_json_string(self):
        """Return dictionary representation of Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def area(self):
        """Return area of Square"""
        return self.width * self.height

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
