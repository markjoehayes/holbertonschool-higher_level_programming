#!/usr/bin/python3
"""Module to convert an object to JSON"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object as a string"""
    return json.dumps(my_obj)
