#!/usr/bin/python3
def safe_print_integer(value):
    """Print the value if it is an integea, returns False otherwiser"""
    try:
        print("{:d}".format(value))
    except TypeError, ValueError:
        return False
    return True
