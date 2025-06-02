#!/usr/bin/python3
"""define a function that writes to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file and return  number of chars written"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return (len(list(text)))
