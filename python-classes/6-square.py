#!/usr/bin/python3
"""define a class Square by size"""


class Square:
    """Represents a square with a size"""
    def __init__(self, size=0, position=(0,0)):
        """initialize the data"""

        self.size = size
        self.positon = position

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

    @property
    def position(self):
        """Getting method"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
