#!/usr/bin/python3
"""A module to define a rectangle"""


class Rectangle:
    """A class to define a rectangle"""
    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self._width

    @width.setter
    def width(self, value):
        """setter for width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value


    @property
    def height(self):
        """Getter for height"""
        return self._height

    @width.setter
    def height(self, value):
        """Setter for height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
