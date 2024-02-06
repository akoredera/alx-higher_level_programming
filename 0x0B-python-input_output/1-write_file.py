#!/usr/bin/python3
'''
Write to a file
'''


def write_file(filename="", text=""):
    '''reads a text file (UTF8) and prints it to stdout'''
    with open(filename, 'w', encoding="UTF-8") as fileOpen:
        return fileOpen.write(text)
