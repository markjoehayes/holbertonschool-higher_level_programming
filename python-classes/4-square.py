#!/usr/bin/python3
"""define a class Square by size"""


class Square:
    """Represents a square with a size"""
    def __init__(self, size=0):
        """initialize the data"""

        self.size = size

        @property
        def size(self):
            """Get/set current size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        """calculate the are of Square"""
        return (self.__size ** 2)
