#!/usr/bin/python3
"""Module that contains class MyList that inherits from list"""

class MyList(list):
    """Defines the MyList class"""

    def print_soirted(self):
        """prints the sorted list"""
        print(sorted(self))
