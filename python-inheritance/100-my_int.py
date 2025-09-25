#!/usr/bin/python3
"""Module to create a rebel integer"""


class MyInt(int):
    """defines a rebel integer class called MyInt"""

    def __eq__(self, value):
        """exchange == operator with != operator"""
        return self.real != value

    def __ne__(self, value):
        return self.real == value
