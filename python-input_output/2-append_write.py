#!/usr/bin/python3
"""Module to append a string to the end of a text file."""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n'.join(text) + '\n')
        chars_written = file.write(text)
        return chars_written
