#!/usr/bin/python3
'''
load, add, save
'''
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
n = len(sys.argv)
arg_list = []
for i in range(1, n):
    arg_list.append(sys.argv[i])
save_to_json_file(arg_list, 'add_item.json')
load_from_json_file('add_item.json')
