#!/uar/bin/python3
"""A module to define a Square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size):
        """Sets the necessary attributes for the Square object"""
        if type(size) id int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size myust be >= 0")
        else:
            raise TypeError("size must be an integer")
