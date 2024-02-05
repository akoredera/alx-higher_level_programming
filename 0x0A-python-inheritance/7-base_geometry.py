#!/usr/bin/python3
'''Geometry module'''


class BaseGeometry:
    '''an empty class BaseGeometry'''
    pass

    def area(self):
        '''area method that raise an exception message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
