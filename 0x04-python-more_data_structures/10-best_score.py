#!/usr/bin/python3

def best_score(a_dictionary):
    '''function returns a key with the biggest integer value.'''
    if a_dictionary:
        new_dic = max(a_dictionary, default=None, key=a_dictionary.get)
        return new_dic
