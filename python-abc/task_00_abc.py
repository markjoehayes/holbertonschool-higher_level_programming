#!/usr/bin/python3
"""create an abstract Animal class with two subclasses: Dog and Cat"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """class to define Animal"""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """class to defina an animal, Dog"""

    def sound(self):
        """returns the sound a dog makes"""
        return "Bark"

class Cat(Animal):
    """class to define another animal, Cat"""

    def sound(self):
        """returns the sound a cat makes"""
        return "Meow"
