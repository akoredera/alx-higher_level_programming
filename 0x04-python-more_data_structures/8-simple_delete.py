#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """function deletes a key in a dictionary."""
    if a_dictionary:
        if key in a_dictionary.keys():
            del a_dictionary[key]
            return a_dictionary
        else:
            return a_dictionary
