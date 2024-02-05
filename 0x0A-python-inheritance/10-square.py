#!/usr/bin/python3
'''Square module that inherit from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''

    def __init__(self, size):
        '''constructor'''
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
