#!/usr/bin/python3

def weight_average(my_list=[]):
    '''function returns the weighted average
    of all integers tuple (<score>, <weight>)'''
    if my_list:
        score_list = []
        weight_list = []
        weight = 0
        score = 0

        for i in my_list:
            mul = 1
            for j in i:
                mul *= j
            score_list.append(j)
            weight_list.append(mul)
        for i in score_list:
            score += i
        for j in weight_list:
            weight += j
        return weight / score
    else:
        return 0
