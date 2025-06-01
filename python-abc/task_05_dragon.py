#!/usr/bin/python3
class SwimMixin:
    """A mixin to help design a creature that swims"""
    def swim(self):
        """Show the creature swimming"""
        print("The ctreature swims!")

class FlyMixin:
    """A mixin to help the creature fly"""
    def fly(self):
        """Show the creature flying"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """A Dragon Class that inherts from Swim and Fly Mixins"""
    def roar(self):
        """Additional methods to make the dragon roar"""
        print("The dragon roars!")

if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
    print(Dragon.mro())
