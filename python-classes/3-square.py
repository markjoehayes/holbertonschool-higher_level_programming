#!/usr/bin/python3
"""A module to define a Square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Retuns the current square area"""
        return self.__size**2
