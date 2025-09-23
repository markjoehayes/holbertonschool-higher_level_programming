#!/usr/bin/python3
"""Module to test if object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """return True if object is an instance of the class"""
    if isinstance(obj, a_class):
        return True
    return False
