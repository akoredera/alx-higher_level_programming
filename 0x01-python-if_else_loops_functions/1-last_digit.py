#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
num_str = list(num_str)
num_str = num_str[-1]
last_number = int(num_str)
if number >= 0:
    if last_number > 5:
        print("Last digit of {} is {} is greater than 5".format(number, last_number))
    elif last_number == 0:
        print("Last digit of {} is {} is zero".format(number, last_number))
    elif last_number < 6 and last_number != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_number))
else:
    if last_number < 6 and last_number != 0:
        print("Last digit of {} is {: d} and is less than 6 and not 0".format(number, (- last_number)))
