#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method for defining the sound an animal makes"""
        pass

class Dog(Animal):
    """Dog class inherited from Animal"""

    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"

class Cat(Animal):
    """Cat class inherited from Animal"""

    def sound(self):
        """returns the sound a cat makes"""
        return "Meow"
