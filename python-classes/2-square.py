#!/usr/bin/python3
"""define a class Square by size"""


class Square:
    """Represents a square with a size"""
    def __init__(self, size=0):
        """initialize the data"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
