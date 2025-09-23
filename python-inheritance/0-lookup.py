#!/usr/bin/python3
"""Module to list avaiulable attributes and methods of an object"""

def lookup(obj):
    """returns a listr of attriubutes and methods of an object"""
    return dir(obj)
