#!/usr/bin/python3
"""
module rectangle contain the real definition of rectangle
"""


class Rectangle:
    """ Rectangle class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """instantiation method with keyword parameters

        Args:
            width: a keyword parameter with a default value of 0
            height: a keyword parameter with a default value of 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width private instance atrribute that retrive and set'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height private instance atrribute that retrive and set'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method rerutn the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """method return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
