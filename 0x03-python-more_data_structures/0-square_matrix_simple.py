#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new = []
    for row in range(len(matrix)):
        new.append(list(map(lambda i: i**2, matrix[row])))
    return new