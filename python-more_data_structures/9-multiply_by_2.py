#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, item in a_dictionary.items():
        a_dictionary[item] = 2 * item
    return a_dictionary
