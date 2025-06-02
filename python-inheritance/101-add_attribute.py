#!/usr/bin/python

def add_attribute(obj, att, value):
    """Add an attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute'")
    setattr(obj, att, value)
