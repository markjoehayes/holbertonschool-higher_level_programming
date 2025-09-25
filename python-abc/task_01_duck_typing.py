#!/usr/bin/python3
"""Module to define an abstract shape class"""

from abc import ABC, abstractmethod
import math

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
        return math.pi * (self.radius**2)

    def perimeter(self):
        """returns the circle's perimeter'"""
        return 2 * (math.pi * self.radius)

class Rectangle(Shape):
    """class to define a Rectangle"""
    def __init__(self, width, height):
        """initialize a new Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the Rectangle"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Prints the area and perimeter of any shape object"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Test the Code

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle info:")
    shape_info(circle)

    print("\nRectangle Info:")
    shape_info(rectangle)
