#!/usr/bin/python3
import py_compile


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def square_matrix_simple(matrix=[]):
    [[row[i] for row in matrix] for i in range(3)]



new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

filename = '0-square_matrix_simple.py'
compile()
