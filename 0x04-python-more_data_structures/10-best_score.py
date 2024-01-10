#!/usr/bin/python3

def best_score(a_dictionary):
    '''function returns a key with the biggest integer value.'''
    new_dic = sorted(a_dictionary)
    return new_dic[-1]
