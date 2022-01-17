#!/usr/bin/python3


class Rectangle:
    def __init__(self, width, height):
        """
        Initializes the rectangle.
        `width` and `height` must be integers and >= 0.
        `pep8` recommends to use `self.__width` instead of `self.width`.
        Returns:
            None
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width.
        Returns: int: The width of the rectangle.
        Raises: TypeError: If width is not an integer.
        """
        if self.width is not (type(int)):
            raise TypeError("width must be an integer")
        elif self.width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width

    @property
    def height(self):
        """Getter for height.
        Returns: int: The height of the rectangle.
        Raises: TypeError: If height is not an integer.
        """
        if self.height is not (type(int)):
            raise TypeError("height must be an integer")
        elif self.height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height

    @width.setter(self, value):
    """ Setter for width.
    Returns: int: The width of the rectangle.
    Raises: TypeError: If width is not an integer.
    """
    pass
