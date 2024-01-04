#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    counter = 0
    sum_argv = 0
    arg_len = len(sys.argv)
    for i in range(1, arg_len):
        if sys.argv[1] == "":
            break
        counter += 1
        sum_argv += int(sys.argv[counter])
    if len(sys.argv) == 1:
        print("{}".format(0))
    else:
        print(sum_argv)
