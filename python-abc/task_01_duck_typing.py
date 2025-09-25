#!/usr/bin/python3
"""Module to define an abstract shape class"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """class to define an abstract shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """class to define a circle"""
    def __init__(self, radius):
        """initializer a new Circle"""
        self.radius = radius

    def area(self):
        """returns the circle's area"""
        return 3.14 * (radius**2)

    def perimeter(self):
        """returns the circle's perimeter'"""
        return 2 * (3.14 * radius)

class Rectangle(Shape):
    """class to define a Rectangle"""
    def __init__(self, width, height):
        """initialize a new Rectangle"""
        self.length = width
        self.width = height

    def area(self):
        """returns the area of a rectangle"""
        return width * height

    def perimeter(self):
        """returns the perimeter of the Rectangle"""
        return 2 * (width + height)
