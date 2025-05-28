#!/usr/bin/python3
"""BaseGeometry class with strict integer validation."""


class BaseGeometry:
    """Empty class with area and validator methods."""

    def area(self):
        """Raise area-not-implemented exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as integer.
        
        Args:
            name: Always a string
            value: Must be positive integer
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
