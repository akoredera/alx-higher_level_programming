#!/usr/bin/python3

'''
function that prints x elements of a list
'''


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[:x]:
            print(i, end="")
            count += 1
    except IndexError as err:
        print(err)
    print('')
    return (count)
