#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for p in range(len(matrix)):
        new_matrix += [list(map(lambda x: x ** 2, matrix[p]))]
    return new_matrix
