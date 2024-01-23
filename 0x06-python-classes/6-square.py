#!/usr/bin/python3

'''file contain a class that defines a square'''


class Square:
    '''class square defines a square'''
    def __init__(self, size=0, position=(0,0)):
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
        else:
            sqr_char = "#" * self.size
            #pos = self.position
            #space = "_" * pos[0]
            for i in range(self.size):
                '''
                if pos[0] > 0:
                    print(space, end="")
                    '''
                print(sqr_char)


    @property
    def position(self):
        '''retrieve property'''
        return self.__position

    @size.setter
    def position(self, value):
        '''setter property'''
        if type(value) == tuple:
            for i in value:
                if i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
                    break
                else:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
