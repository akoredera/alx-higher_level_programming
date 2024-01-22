#!/usr/bin/python3
import sys

"""function that prints an integer"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        result = "Exception: {}\n".format(err)
        sys.stderr.write(result)
        return False
