#!/usr/bin/python3
'''
Exact same object task
'''

def is_same_class(obj, a_class):
    '''
    returns True if the object is exactly an instance of the specified class
    '''
    return type(obj) == a_class
