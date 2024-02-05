#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a child that inherit from the parent list class"""
    def print_sorted(self):
        '''method print sorted list'''
        result = sorted(self)
        print(result)
