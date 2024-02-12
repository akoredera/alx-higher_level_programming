#!usr/bin/python3
'''First rectangle'''

from models.base import Base
'''import class Base from models/base module'''


class Rectangle(Base):
    '''class Rectangle child of Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter and setter method for width with private attribute'''
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''getter and setter method for height with private attribute'''
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def x(self):
        '''getter and setter method for x with private attribute'''
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''getter and setter method for width y private attribute'''
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        '''returns the area value of the rectangle instance'''
        return self.width * self.height

    def display(self):
        '''prints in stdout the rectangle instance with the character #'''
        for i in range(self.y):
            print()
        for x in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''overriding __str__ method'''
        return "[Rectangle]({:d}) {:d}/{:d}\
        - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''
        method update the class Rectangle by
        assigning an argument to each attribute
        '''
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.__width = args[arg]
                if arg == 2:
                    self.__height = args[arg]
                if arg == 3:
                    self.__x = args[arg]
                if arg == 4:
                    self.__y = args[arg]

    def to_dictionary(self):
        '''
        return the dictionary
        representation of a Rectangle
        '''
        return dict(x=self.x, y=self.y, id=self.id,
                    height=self.height, width=self.width)
