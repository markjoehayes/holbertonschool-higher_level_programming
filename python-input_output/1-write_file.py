#!/usr/bin/python3
"""Module to open a file and write to it """


def write_file(filename="", text=""):
    """function to write a string to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
