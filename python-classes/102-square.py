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

    def __eq__(self, other):
        """Check if two squares have equal area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if current square's area is greater than another"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if current square's area is greater or equal to another"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if current square's area is less than another"""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if current square's area is less or equal to another"""
        return self.area() <= other.area()
