#!/usr/bin/python3
"""Module to convert JSON to python object"""
import json


def from_json_string(my_str):
    """returns a python object from JSON string"""
    return json.loads(my_str)
