#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''function that computes the square value of all integers of a matrix.'''
    matrix_copy = matrix[:]
    for i in range(0, len(matrix) - 1):
        matrix_copy[i] = list(map((lambda x: x ** 2), matrix_copy[i]))

    return matrix_copy
