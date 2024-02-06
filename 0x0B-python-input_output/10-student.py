#!/usr/bin/python3
'''
Student to JSON
'''


class Student:
    '''class student that defines a student'''
    def __init__(self, first_name, last_name, age):
        '''CONSTRUCTOR'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''method retrieves dictionary representation of a Student instance'''
        if isinstance(attrs, list):
            thisdict = {}
            for i in attrs:
                if i == 'first_name':
                    thisdict.update({'first_name': self.first_name})
                elif i == 'last_name':
                    thisdict.update({'last_name': self.last_name})
                elif i == 'age':
                    thisdict.update({'age': self.age})
            return thisdict
        else:
            return {'first_name': self.first_name,
                    'last_name': self.last_name, 'age': self.age}
