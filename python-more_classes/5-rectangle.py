#!/usr/bin/python3
"""a class to define a rectangle"""


class Rectangle:
    """Start class Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__height) + (2 * self.__width))

    def area(self):
        """Calculate the area of a rectangle"""
        return (self.__height * self.__width)

    def print(self):
        if self.__width == 0 or self.__height == 0:
            print()
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Return the string representation of a triangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle"""
        print("Bye rectangle...")
