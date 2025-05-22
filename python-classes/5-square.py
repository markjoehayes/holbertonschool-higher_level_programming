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
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """calculate the are of Square"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()

