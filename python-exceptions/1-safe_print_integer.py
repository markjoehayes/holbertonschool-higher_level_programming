#!/usr/bin/python3
def safe_print_integer(value):
    """Print the value if it is an integer"""
    try:
        print("{:d}.format(value)")
    except ValueError:
        return False
    return True
