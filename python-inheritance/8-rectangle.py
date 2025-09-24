#!/usr/bin/python3
"""Module for a rectangle class that inherets from base_geometry"""

exec(open("7-base_geometry.py").read())

class Rectangle(BaseGeometry):
    """defines a Rectangle class that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """initialize a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
