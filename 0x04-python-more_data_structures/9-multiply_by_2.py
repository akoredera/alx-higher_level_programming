#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """function returns a new dictionary
    with all values multiplied by 2"""
    if a_dictionary:
        new_dictionary = {}
        for i, j in a_dictionary.items():
            new_dictionary[i] = j * 2
        return new_dictionary
