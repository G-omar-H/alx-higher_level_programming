#!/usr/bin/python3
"""
    welcom to the matrix
"""


def matrix_divided(matrix, div):
    """
        function that divides all elements of a matrix
        DOES
            :matrix: matrix to divid
            :type matrix: list
            :div: divider
            :type divider: int float
        RETURN
            a new matrix
    """
    if type(matrix) is not list or matrix == []:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                )
            elif type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
        if len({len(i) for i in matrix}) != 1:
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(float(j / div), 2) for j in i] for i in matrix]
