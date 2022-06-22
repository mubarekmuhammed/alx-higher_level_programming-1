#!/usr/bin/python3
"""Define a class square"""


class Square:
    """representing a square"""

    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the current square area"""
        return self.__size ** 2
