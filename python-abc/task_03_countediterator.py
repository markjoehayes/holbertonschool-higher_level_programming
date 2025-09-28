#!/usr/bin/python3
"""Module to extend the iter builtin"""

class CountedIterator:
    """class to extend the iter builtin"""
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count of items iterated"""
        return self.counter

    def __next__(self):
        """Override the __next__ method to count iteration"""
        try:
            # get the next item from the original iterator
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            # raise the stopIteration exception
            raise

    def __iter__(self):
        """Return self to make CountedIterator iterable"""
        return self

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")

