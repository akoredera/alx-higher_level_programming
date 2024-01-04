#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    counter = 0
    str_list = []
    arg_len = len(sys.argv)
    for i in range(1, arg_len):
        if sys.argv[1] == "":
            break
        counter += 1
        str_list.append(sys.argv[counter])
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(str_list) == 1:
        print("{} argument:".format(len(str_list)))
        print("{}: {}".format(1, str_list[0]))
    else:
        print("{} arguments:".format(len(str_list)))
        counter = 1
        for i in str_list:
            print("{}: {}".format(counter, i))
            counter += 1
