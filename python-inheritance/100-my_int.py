#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """A Class MyInt, a rebel integer"""
    def __equal__(self, value):
        """Change == to !="""
        return self.real != value
    def __notequal__(self, value):
        """Change != to =="""
        return self.real == value
