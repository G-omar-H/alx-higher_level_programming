#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        square_matrix += [list(map(lambda x: x**2, matrix[i]))]
    return square_matrix
