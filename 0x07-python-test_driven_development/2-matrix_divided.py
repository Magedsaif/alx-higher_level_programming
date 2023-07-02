#!/usr/bin/python3
"""Divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (int or float): a list of lists of integers or floats
        div (int or float): must be a number (integer or float)
    Returns:
    result of dividing matrix by div rounded to 2 decimal places
    in a new matrix
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(message)

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    resulted_matrix = []
    for row in matrix:
        for element in row:
            resulted_matrix.append(round(element / div, 2))
    return resulted_matrix
