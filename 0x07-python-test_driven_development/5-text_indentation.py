#!/usr/bin/python3
'''
5-text_indentation 
The 5-text_indentation supplies one function, text_indentation()

'''
def text_indentation(text):
    """
    prints a text with 2 new lines after each
    of these characters: ., ? and :
    args:
    text: string
    """ 
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in [".", '?', ':']:           
            print("{}\n".format(text[i]))
        elif text[i] == " " and text[i - 1] in [".", '?', ':']:
            continue
        else:
            print(text[i], end="")
