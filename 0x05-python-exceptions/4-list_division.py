#!/usr/bin/python3

"""function that divides element by element 2 lists"""


def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    for i in range(list_length):
        try:
            result = my_list_1[i]/my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("Out of range")
        finally:
            list_result.append(result)
    return list_result

