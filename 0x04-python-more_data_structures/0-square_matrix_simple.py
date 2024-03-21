#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''computes the square value of all integers of a matrix.'''
    if matrix is not None:
        new = []
        for row in matrix:
            new.append(list(map(lambda x: x**2, row)))
        return (new)
    return None
