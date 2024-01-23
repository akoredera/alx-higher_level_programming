#!/usr/bin/python3

'''file contain a class that defines a square'''


class Square:
    '''class square defines a square'''
    def __init__(self, size=0):
        '''initialization of object attribute
        Args
        size: size of a square
        '''
        self.__size = size
        if not type(self.__size) == int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
