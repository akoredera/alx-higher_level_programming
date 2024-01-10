#!/usr/bin/python3

def best_score(a_dictionary):
    '''function returns a key with the biggest integer value.'''
    if a_dictionary:
        new_dic = sorted(a_dictionary)
        return new_dic[-1]
