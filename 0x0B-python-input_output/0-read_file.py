#!/usr/bin/python3
'''
Read file
'''


def read_file(filename=""):
    '''reads a text file (UTF8) and prints it to stdout'''
    with open(filename, encoding="UTF-8") as fileOpen:
        print(fileOpen.read())
