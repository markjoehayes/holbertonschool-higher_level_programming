#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(number))
        return True
    except (ValueError, TypeError):
        return False
