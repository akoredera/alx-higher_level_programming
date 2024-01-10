#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """a function that replaces all occurrences
    of an element by another in a new list"""
    if my_list:
        new_list = my_list[:]
        new_list = list(map(lambda x: replace if x == search else x, my_list))
        return new_list