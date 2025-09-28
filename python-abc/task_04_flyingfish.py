#!/usr/bin/python3
"""Module to construct a FlyingFish that inherits from a Fish class and a Bird class"""

class Fish:
    """class to define a Fish"""
    def swim(self):
        """swim method"""
        print("The fish is swimming")

    def habitat(self):
        """habitat method"""
        print("The fish lives in water")

class Bird:
    """class to define a bird"""
    def fly(self):
        """fly method"""
        print("The bird is flying")

    def habitat(self):
        """habitat method"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """class to define a Flying Fish"""
    def fly(self):
        """override the inherited method"""
        print("The flying fish is soaring")

    def swim(self):
        """Overrides the swim method"""
        print("The flying fish is swimming")

    def habitat(self):
        """Overrides the habitat method"""
        print("The flying fish lives both in water and the sky!")

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()
