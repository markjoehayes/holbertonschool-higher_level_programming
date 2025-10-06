#!/usr/bin/env python3
"""
Module for serializing Python dictionaries to XML and deserializing XML back to dictionaries.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.
    
    Args:
        dictionary: A Python dictionary to serialize
        filename: The filename where the XML will be saved
    """
    try:
        # Create the root element
        root = ET.Element("data")
        
        # Iterate through dictionary items and add them as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convert all values to strings for XML
        
        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        raise


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and return a Python dictionary.
    
    Args:
        filename: The filename of the XML file to read
        
    Returns:
        dict: A Python dictionary with the deserialized data
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from XML elements
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
        
        return result_dict
        
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        raise
