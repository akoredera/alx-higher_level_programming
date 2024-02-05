#!/usr/bin/python3
'''
Only sub class of
'''


def inherits_from(obj, a_class):
    '''
    returns True if the object is exactly an instance of a class
    that inherited (directly or indirectly) from the specified class
    '''
    return True if issubclass(type(obj), a_class) and type(obj) != a_class else False
