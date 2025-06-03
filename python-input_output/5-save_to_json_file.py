#!/usr/bin/python3
"""Writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """defines a function that writes an object to a file"""
    with open(filename, mode='w', encoding='UTF-8') as file:
        json.dump(my_obj, file)
