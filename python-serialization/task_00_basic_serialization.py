#!/usr/bin/env python3
"""
Basic serialization module that provides functions for
serializing Python dictionaries to JSON files and
deserializing JSON files back to Python dictionaries.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    
    Args:
        data: A Python Dictionary with data to be serialized
        filename: The filename of the output JSON file. 
                 If the file exists, it will be replaced.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error serializing data to {filename}: {e}")
        raise


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file to a Python dictionary.
    
    Args:
        filename: The filename of the input JSON file
        
    Returns:
        A Python Dictionary with the deserialized JSON data from the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error deserializing data from {filename}: {e}")
        raise
