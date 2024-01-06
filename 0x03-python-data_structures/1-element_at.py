#!/usr/bin/python3

def element_at(my_list, idx):
    """a function that retrieves an element from a list"""
    list_len = len(my_list)
    if idx < 0 or idx >= list_len:
        return None
    else:
        return my_list[idx]
