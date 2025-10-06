#!/usr/bin/env python3
"""
Module to convert CSV files to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to data.json.
    
    Args:
        csv_filename: The name of the CSV file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read data from CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # Use DictReader to convert each row to a dictionary
            csv_reader = csv.DictReader(csv_file)
            # Convert to list of dictionaries
            data = list(csv_reader)
        
        # Write data to JSON file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        
        return True
        
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")
        return False
