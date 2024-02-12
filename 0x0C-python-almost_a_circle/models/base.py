#!/usr/bin/python3
'''Base class'''
import json
''' import json module'''


class Base:
    '''class base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        method return the JSON string
        representation opf list_dictionaries
        '''
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''
        method returns the list of the JSON string
        representation json_String

        Arg:
        json_string: a string representing a list of dictionaries
        '''
        if json_string is None:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        method writes the JSON string
        representation of list_objs to a file
        '''
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as f:
                f.write(cls.to_json_string(list_objs))
        else:
            dict_list = []
            for obj in (list_objs):
                dict_list.append(cls.to_dictionary(obj))
            json_output = cls.to_json_string(dict_list)
            with open(f"{cls.__name__}.json", "w") as f:
                f.write(json_output)

    @classmethod
    def create(cls, **dictionary):
        '''
        method returns an instance with
        all atributes already set
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy_instance = cls(1)
            elif cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            dummy_instance.update(**dictionary)
            return dummy_instance
