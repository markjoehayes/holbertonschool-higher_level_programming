#!/usr/bin/python3
"""A function to return JSON representation"""


import json


def to_json_string(my_obj):
    """define a function that returns a JSON representation of a string"""
    return json.dumps(my_obj)
