#!/usr/bin/python3
"""Define a class square"""


class Square:
    """representing a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """retrieves the size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Returns the current square area"""
        return self.__size ** 2
