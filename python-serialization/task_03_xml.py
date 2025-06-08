import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file
    
    Args:
        dictionary: The dictionary to serialize
        filename: The output XML filename
        
    Returns:
        None
    """
    try:
        # Create the root element
        root = ET.Element("data")
        
        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        # Create element tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        raise

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary
    
    Args:
        filename: The XML file to read
        
    Returns:
        dict: The deserialized dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
        
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        raise
