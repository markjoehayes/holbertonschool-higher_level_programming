#!/usr/bin/python3
"""A module to define a Square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0,0)):
        """Sets the necessary attributes for the Square object"""
        self.size = size
        self.position = position

    def area(self):
        """Retuns the current square area"""
        return self.__size**2

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter for the position with validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints to stdout the square with #"""
        if self.__size == 0:
            print('')
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print('')
