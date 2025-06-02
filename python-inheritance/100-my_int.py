#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """A Class MyInt, a rebel integer"""
    def __eq__(self, value):
        """Change == to !="""
        if isinstance(self, type(value)):
            return False
    def __ne__(self, value):
        """Change != to =="""
        if isinstance(self, type(value)):
            return True
