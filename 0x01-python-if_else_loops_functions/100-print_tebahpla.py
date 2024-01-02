#!/usr/bin/python3
j = 25
for i in range(97, 123):
    k = i + j
    if k % 2 != 0:
        print("{}".format(chr(k-32)), end="")
    else:
        print("{}".format(chr(k)), end="")
    j -= 2
