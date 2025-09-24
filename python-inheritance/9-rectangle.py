#!/usr/bin/python3
"""Module for a rectangle class that inherets from base_geometry"""

base_geometry = __import__('7-base_geometry')
BaseGeometry = base_geometry.BaseGeometry


class Rectangle(BaseGeometry):
    """defines a Rectangle class that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """initialize a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
