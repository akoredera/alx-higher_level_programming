#!/usr/bin/python3
'''
Save Object to a file
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    writes an Object to a text file,
    using a JSON representation
    '''
    with open(filename, 'w', encoding="utf-8") as save_file:
        json_file = json.dumps(my_obj)
        save_file.write(json_file)
