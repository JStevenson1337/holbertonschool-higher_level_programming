#!/usr/bin/python3
""" A Rectangle Class """


class Rectangle:
    """
        Class Rectangle:
    """
    def __init__(self, width, height):
        """
            __init__ method:
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Returns the width of the rectangle.
            Returns:
                The width of the rectangle
        """
        return self.__width


    @property
    def height(self):
        """
            Returns the height of the rectangle.
            Returns:
                The height of the rectangle
        """
        return self.__height


    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            return (self.__width = value)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            return (self.__height = value)


my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)


try:
    my_rectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(-2, 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

