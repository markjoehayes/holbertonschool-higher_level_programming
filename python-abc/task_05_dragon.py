#!/usr/bin/python3
"""Mixin Classes"""

class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon Class using Mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
    
    def breathe_fire(self):
        print("The dragon breathes fire!")

# Testing the Dragon's Abilities
if __name__ == "__main__":
    print("=== Testing Dragon Class with Mixins ===")
    
    # Instantiate a Dragon object
    draco = Dragon()
    
    # Demonstrate all abilities
    print("\n--- Dragon's Abilities ---")
    draco.swim()        # From SwimMixin
    draco.fly()         # From FlyMixin
    draco.roar()        # From Dragon class
    draco.breathe_fire()  # Additional Dragon method
    
    # Testing with multiple instances
    print("\n--- Multiple Dragons ---")
    smaug = Dragon()
    toothless = Dragon()
    
    print("Smaug:")
    smaug.fly()
    smaug.breathe_fire()
    
    print("Toothless:")
    toothless.swim()
    toothless.roar()
    
    # Demonstrate mixin reusability
    print("\n--- Mixin Reusability Examples ---")
    
    # Other creatures using the same mixins
    class Duck(SwimMixin, FlyMixin):
        def quack(self):
            print("The duck quacks!")
    
    class Seaplane(SwimMixin, FlyMixin):
        def takeoff(self):
            print("The seaplane takes off from water!")
    
    class Merperson(SwimMixin):
        def sing(self):
            print("The merperson sings beautifully!")
    
    # Test other creatures
    donald = Duck()
    print("\nDuck abilities:")
    donald.swim()
    donald.fly()
    donald.quack()
    
    hydro = Seaplane()
    print("\nSeaplane abilities:")
    hydro.swim()
    hydro.fly()
    hydro.takeoff()
    
    ariel = Merperson()
    print("\nMerperson abilities:")
    ariel.swim()
    ariel.sing()
    
    # Method Resolution Order demonstration
    print("\n--- Method Resolution Order ---")
    print("Dragon MRO:", Dragon.__mro__)
    print("Duck MRO:", Duck.__mro__)
    print("Seaplane MRO:", Seaplane.__mro__)
    
    # Testing inheritance and isinstance
    print("\n--- Type Checking ---")
    print(f"Is draco a Dragon? {isinstance(draco, Dragon)}")
    print(f"Is draco a SwimMixin? {isinstance(draco, SwimMixin)}")
    print(f"Is draco a FlyMixin? {isinstance(draco, FlyMixin)}")
    print(f"Is donald a Duck? {isinstance(donald, Duck)}")
    print(f"Is donald a SwimMixin? {isinstance(donald, SwimMixin)}")

    # Advanced: Dynamic mixin usage
    print("\n--- Dynamic Behavior Composition ---")
    
    def create_hybrid_creature(*mixins, class_name="HybridCreature"):
        """Dynamically create a class with specified mixins"""
        return type(class_name, mixins, {})
    
    # Create a flying fish dynamically
    FlyingFish = create_hybrid_creature(SwimMixin, FlyMixin, class_name="FlyingFish")
    flying_fish = FlyingFish()
    print("Dynamically created FlyingFish:")
    flying_fish.swim()
    flying_fish.fly()

    # Complex hybrid
    class MagicMixin:
        def cast_spell(self):
            print("The creature casts a magic spell!")
    
    class FireMixin:
        def breathe_fire(self):
            print("The creature breathes fire!")
    
    # Create a complex hybrid
    class MagicalFireDragon(Dragon, MagicMixin, FireMixin):
        def teleport(self):
            print("The dragon teleports!")
    
    print("\n--- Complex Hybrid Dragon ---")
    complex_dragon = MagicalFireDragon()
    complex_dragon.swim()
    complex_dragon.fly()
    complex_dragon.roar()
    complex_dragon.cast_spell()
    complex_dragon.breathe_fire()  # This will use FireMixin's method due to MRO
    complex_dragon.teleport()
