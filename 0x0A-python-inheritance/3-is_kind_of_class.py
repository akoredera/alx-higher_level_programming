#!/usr/bin/python3
'''
Exact same object task
'''


def is_kind_of_class(obj, a_class):
    '''
    returns True if the object is exactly an instance of the specified class
    '''
    return True if isinstance(obj, a_class) else False
