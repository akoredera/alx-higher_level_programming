#!/usr/bin/python3
'''
And now, the square
'''
from models.rectangle import Rectangle
'''import Rectangle class from models.rectangle'''


class Square(Rectangle):
    '''
    class Square a child to class
    Rectangle and grand child of base
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''square constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str method to override'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    @property
    def size(self):
        '''public getter and setter method for size'''
        return (self.width, self.height)

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size < 0:
            raise ValueError("width must be >= 0")
        else:
            width, height = size, size

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key ==  'size':
                    self.width, self.height = value, value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width, self.height = args[i], args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]


    def to_dictionary(self):
        '''return the dictionary representation of a Rectangle'''
        return dict(x=self.x, y=self.y, id=self.id, size=self.width)
