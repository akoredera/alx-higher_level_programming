#!/usr/bin/python3

'''file contain a class that defines a square'''


class Square:
    '''class square defines a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''initialization of object attribute
        Args
        size: size of a square
        position: a tuple of 2 positive integers
        '''
        self.size = size
        self.position = position
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

    def my_print(self):
        '''print in stdout the square with the character #'''
        if self.size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def position(self):
        '''retrieve property'''
        return self.__position

    @position.setter
    def position(self, value):
        '''setter property'''
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
