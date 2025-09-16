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
    
    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value
