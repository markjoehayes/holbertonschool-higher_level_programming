#!/usr/bin/python3
"""Module to write an object to a text file in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
