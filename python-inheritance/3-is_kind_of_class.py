#!/usr/bin/python3
"""Module to test is object is instance of or if the object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """Return True if isinstance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
