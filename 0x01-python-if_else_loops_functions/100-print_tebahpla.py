#!/usr/bin/python3
j = 25
for i in range(97, 123):
    k = i + j
    if k % 2 != 0:
        value = k - 32
    else:
        value = k
    print("{}".format(chr(value)), end="")
    j -= 2
