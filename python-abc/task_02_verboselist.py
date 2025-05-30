#!/usr/bin/python3

class VerboseList(list):
    """A list that prints notifications in modifications"""

    def append(self, item):
        """Add an item to the end of the list and print a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend a list by appending elements from iterable and print a notification"""
        super().extend(iterable)
        print(f"Extend the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove the first occurance of the item and print a notification"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Remove and retuen item at index (default last) and print notification"""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

