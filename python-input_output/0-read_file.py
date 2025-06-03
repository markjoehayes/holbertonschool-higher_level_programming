#!/usr/bin/python3
"""Write a function that reads a text file"""


def read_file(filename=""):
    """Print the contents of a UTF-8 textfile to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
