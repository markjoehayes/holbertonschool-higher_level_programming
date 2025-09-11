#!/usr/bin/python3
def only_diff_elements(set1, set2):
    differents = set()
    for element in set1:
        if element not in set2:
            differents.add(element)
    for elements in set2:
        if element not in differents:
            differents.add(element)
    return differents
