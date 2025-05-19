#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, bool):
            return False
        number = int(value)
        print("{:d}".format(number))
        return True
    except (ValueError, TypeError):
        return False
