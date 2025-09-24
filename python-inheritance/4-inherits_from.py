#!/usr/bin/python3
"""Module to check if object is instance of a subclass, but not he class"""


def inherits_from(obj, a_class):
    """return true if the object is instance of an inherited class"""
    #Get the class of the object
    obj_class = type(obj)
    #Check if it is a subclass, but not the main class
    if obj_class is not a_class and issubclass(obj_class, a_class):
        return True
    return False
