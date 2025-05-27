#!/usr/bin/python3
"""return attributes and methods of an object"""
def lookup(obj):
    """function to return all the attributes and methods of an object"""
    return (list(dir(obj)))
