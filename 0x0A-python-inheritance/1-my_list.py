#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a child that inherit from the parent list class"""
    def __init__(self):
        """initialization of self and the parent class"""
        super().__init__(self)

    def print_sorted(self):
        '''method print sorted list'''
        result = sorted(self)
        print(result)
