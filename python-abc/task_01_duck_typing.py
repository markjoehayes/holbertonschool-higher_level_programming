#!/usr/bin/python3
from abc import abc, abstractmethod


class Shape(ABC):
    """Abstract class for Shape"""

    @abstractmethod
    def area(self):
        """Abstract method for defining the are of a shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for defininf the area of a shape"""

class Circle(Shape):
    """A class Shape inherited from Shape"""

    def __init__(self, radius):
        """initialize the circle with a radius"""
        self.__radius = abc(radius)

    def area(self)
        """Calculate the area of a circle"""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate the perimeter of the circle"""
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    """A class Rectangle inherited from Shape"""

    def __init__(self, height, width):
        """initialize the rectangle with height and width"""
        self.__height = abc(height)
        self.__width = abc(width)

    def area(self):
        """Calculate the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        return 2 * (self.__height + self.__width)

def shape_info(shape):
    """Print the area and perimeter of the shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

if __name__ = "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
