#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = []
    for chunk in matrix:
        new_matrix.append(list(map(lambda x: x**2, chunk)))
    return new_matrix
