#!/usr/bin/python3
"""
matrix_divided:
    Divides all values of a matrix
    Returns a new matrix of integers
"""



def matrix_divided(matrix, div):
    """divides all elements of a matrix by div
    checks for proper usage of matrix and div elements
    """
    matErr = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if type(matrix) is not list:
        raise TypeError(matErr)

    if div == 0:
        raise ZeroDivisionError('division by zero')

    size = len(matrix[0])
    for line in matrix:
        if type(line) is not list:
            raise TypeError(matErr)
        if len(line) is not size:
            raise TypeError('Each row of the matrix must have the same size')
        for num in line:
            if type(num) is not int and type(num) is not float:
                raise TypeError(matErr)
    return [[round(num / div, 2) for num in list] for list in matrix]
