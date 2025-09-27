#!/usr/bin/python3
"""Module to extend python's list class"""


class VerboseList(list):
    """defines a class VerboseList that extends list"""

    def append(self, item):
        """Overrides append method in order to print notice after adding item"""
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, iterable):
        """Overrides extend method to print a notice after extending list"""
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Overrides remove method to print a notice every time an item is removed"""
        print(f"Removed {[item]} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Overides the pop method to print a notice everytime an item is popped"""
        item = self[index]
        print(f"Popped {[item]} from the list.")
        super().pop(index)

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)
