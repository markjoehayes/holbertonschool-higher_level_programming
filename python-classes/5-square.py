#!/usr/bin/python3
"""A module to define a Square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object"""
        self.size = size

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints to stdout the square with #"""
        if self.size == 0:
            print('')
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print('')

