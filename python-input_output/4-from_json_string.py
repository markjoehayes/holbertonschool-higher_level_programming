#!/usr/bin/python3
"""returns an obj represented by a json string"""


import json


def from_json_string(my_str):
    """define a function to return an object defined by a json string"""
    return json.loads(my_str)
