import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save to file
        
        Args:
            filename: The file to save the serialized object to
            
        Returns:
            None if serialization fails
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PicklingError, IOError, Exception):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from file
        
        Args:
            filename: The file to load the serialized object from
            
        Returns:
            CustomObject instance or None if deserialization fails
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (pickle.UnpicklingError, FileNotFoundError, EOFError, Exception):
            return None
