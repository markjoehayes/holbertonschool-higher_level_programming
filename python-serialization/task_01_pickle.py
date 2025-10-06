#!/usr/bin/env python3
"""
Custom object class with pickle serialization capabilities.
"""

import pickle


class CustomObject:
    """
    A custom Python class that can be serialized and deserialized using pickle.
    """
    
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize a CustomObject instance.
        
        Args:
            name: A string representing the name
            age: An integer representing the age
            is_student: A boolean indicating student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename: str):
        """
        Serialize the current instance and save it to a file using pickle.
        
        Args:
            filename: The filename where the object will be serialized
            
        Returns:
            None if an error occurs, otherwise saves the file
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object to {filename}: {e}")
            return None
    
    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize an instance from a file using pickle.
        
        Args:
            filename: The filename from which to load the object
            
        Returns:
            CustomObject instance if successful, None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print(f"Error: Loaded object is not an instance of {cls.__name__}")
                    return None
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            return None
        except Exception as e:
            print(f"Error deserializing object from {filename}: {e}")
            return None
