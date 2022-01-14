#!/usr/bin/python3
""" Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix
    Args:
        matrix ([[list]]):
        div (int or float): division value
    Returns:
        matrix:
    """
    if not check_len(matrix):
        raise TypeError("Each row of the matrix must have the same size")


def looping_the_matrix(matrix):
    """ Function to iterate over the matrices

    Args:
        matrix ([[list]]): matrixt to loop over
    """
    for i in matrix:
            for j in i:
                print(j, type(j))
            print(i, type(i))
    return (matrix[i][j])

def check_len(matrix):
    """[summary]

    Args:
        matrix ([type]): [description]
    """
    looper = iter(matrix)
    measure = len(next(looper))
    if not all(len(l) == measure for l in looper):
        return False
    else:
        return True



matrix = [
    [1, 2, 3, 5],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)


# if len({len(i) for i in lists}) == 1:   #list comprehension to preserver length
