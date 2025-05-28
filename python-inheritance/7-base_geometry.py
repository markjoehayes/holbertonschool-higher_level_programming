#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Empty class"""
    
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate integer"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
