#!/usr/bin/python3
''' Can I?'''


def add_attribute(a, name, value):
    ''' adds a new attribute to an object if it’s possible'''
    b = type(a)
    if hasattr(a, '__dict__') or \
            (hasattr(b, '__slots__') and isinstance(a.__slots__, property)):
        setattr(a, name, value)
    else:
        raise TypeError("can't add new attribute")
