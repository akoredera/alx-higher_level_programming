#!/usr/bin/python3

def roman_to_int(roman_string):
    '''function converts a Roman numeral to an integer.'''
    if roman_string == "":
        return 0
    rom_num = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    actual = 0
    diff = 0
    for i in roman_string:
        if rom_num.get(i) < actual:
            actual += rom_num.get(i)
        else:
            diff = rom_num.get(i) - actual
            actual = diff
    return actual
