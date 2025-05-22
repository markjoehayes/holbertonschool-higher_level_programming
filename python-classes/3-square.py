#!/usr/bin/python3
"""define a class Square by size"""


class Square:
    """Represents a square with a size"""
    def __init__(self, size=0):
        """initialize the data"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """calculate the are of Square"""
        return (self.__size ** 2)
