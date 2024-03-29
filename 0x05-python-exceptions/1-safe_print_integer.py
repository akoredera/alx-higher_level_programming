#!/usr/bin/python3
"""function that prints an integer with "{:d}".format()."""


def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        raise Exception
    except Exception:
        return False
