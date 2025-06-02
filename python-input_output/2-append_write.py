#!/usr/bin/python3
"""defines a function for appending a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return (len(list(text)))
