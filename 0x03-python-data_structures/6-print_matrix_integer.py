#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if (j != len(matrix[i]) - 1):
                print(' ', end="")
        print()
        i += 1
