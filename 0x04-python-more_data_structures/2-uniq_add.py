#!/usr/bin/python3

def uniq_add(my_list=[]):
    """a function that adds all unique
    integers in a list (only once for each integer)."""
    if my_list:
        result = 0
        my_list = list(set(my_list))
        for i in range(0, len(my_list)):
            result += my_list[i]
        return result
