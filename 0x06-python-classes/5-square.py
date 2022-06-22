#!/usr/bin/python3
"""Define a class square"""


class Square:
    """representing a square
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0):
        """Initializes the object."""
        self.__size = size

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range (0, self.__size):
                for j in range (0, self.__size):
                    print("#", end="")
                print()
