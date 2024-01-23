#!/usr/bin/python3

'''file contain a class that defines a square'''


class Square:
    '''class square defines a square'''
    def __init__(self, size=0):
        '''initialization of object attribute
        Args
        size: size of a square
        '''
        self.size = size
        '''
        if not type(self.__size) == int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")'''

    def area(self):
        '''returns the current square area'''
        return self.__size ** 2

    @property
    def size(self):
        '''retrieve property'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter property'''
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
