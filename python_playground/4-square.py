#!/usr/bin/python3
"""A simple Square class that defines a square by its size."""


from dis import disassemble


class Square:
    """A simple Square class that defines a square by its size.

    Attributes:
        __size (int): The size of the square.

        Return:
            int : The area of the square.

        Raise:
            TypeError: size must be an integer
            ValueError: size must be >= 0
    """
    def __init__(self, size=0):
        """Initializes the square.
        `size` must be an integer and >= 0.
        `pep8` recommends to use `self.__size` instead of `self.size`.
        Returns:
            None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Finds the area of the square.

        Returns:
            int : The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for size.

        Returns:
            int : The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size.

        Returns:
            int : The Value of the size.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
            """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @size.getter
    def size(self):
        """Getter for size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            int : The size of the square.
        """
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size


    def my_print(self):
        """Prints to stdout the square with the character.
                Prints # if size is 0.
                Prints # * size times.

            Returns:
                None
        """
        if self.__size <= 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#")
            print()

import dis

print(getattr(Square, "__doc__"))
print(Square.my_print.__doc__)

# print(Square.area.__doc__)
# print(Square.size.__doc__)
# print(Square.__doc__)
