#!/usr/bin/python3

def print_last_digit(number):
    num_to_list = list(str(number))
    print("{}".format(num_to_list[-1]), end="")
    return num_to_list[-1]
