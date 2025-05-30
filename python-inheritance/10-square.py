#!/usr/bin/python3
"""Modul for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass representing a Square"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of square"""
        return (self.__size * self.__size)
