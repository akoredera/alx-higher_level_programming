#!/usr/bin/python3
'''
Student to JSON
'''
import json


class Student:
    '''class student that defines a student'''
    def __init__(self, first_name, last_name, age):
        '''CONSTRUCTOR'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method retrieves dictionary representation of a Student instance'''
        return {'first_name': self.first_name,
                'last_name': self.last_name, 'age': self.age}
