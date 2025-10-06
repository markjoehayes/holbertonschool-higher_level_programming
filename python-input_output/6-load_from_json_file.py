#!/usr/bin/python3
"""Module to create an object from a json file"""
import json


def load_from_json_file(filename):
    """function to create an object from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        json.loads(f)
