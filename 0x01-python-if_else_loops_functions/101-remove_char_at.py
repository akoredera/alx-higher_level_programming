#!/usr/bin/python3
def remove_char_at(str, n):
    counter = 0
    char_list = []
    for i in str:
        if counter == n:
            counter += 1
            continue
        char_list.append(i)
        counter += 1
    return ''.join(char_list)
