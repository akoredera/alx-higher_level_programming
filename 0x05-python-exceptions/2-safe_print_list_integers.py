#!/usr/bin/python3
"""
function that prints the first x
elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        if not isinstance(my_list[i], int):
            continue
        print(my_list[i], end="")
        count += 1
    print("")
    return (count)
