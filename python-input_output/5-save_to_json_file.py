#!/usr/bin/python3
"""Module to write an object to a text file in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    filename = json.dumps(my_obj)
    with open("filename", "w") as f:
        f.write(filename)
