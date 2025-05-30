#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry Class"""

    def area(self):
        """Method to compuet this area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for Validating the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
