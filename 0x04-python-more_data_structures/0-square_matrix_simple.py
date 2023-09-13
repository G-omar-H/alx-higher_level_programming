#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        squares = list(map(lambda x: x**2, matrix[i]))
        square_matrix += [squares]
    return square_matrix
