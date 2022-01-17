#!/usr/bin/python3
""" Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Controlls the flow of the program
    Args:
        matrix ([[list]]): list of lists
        div (int or float): division value
    Returns:  list of lists
    """
    try:
        identify(matrix)
        measure(matrix)
        mutate(matrix, div)
        result = mutate(matrix, div)
    except Exception as e:
        print(e)
        return None
    else:
        if result is None:
            return None
        else:
            return split_list(result, len(matrix))


def split_list(a_list, number):
    """ Split list into equal parts
    Args:
        a_list ([[list]]): list to split
        number (int): number of parts
    Returns:
        list: list of lists
    """
    splitNumber = len(a_list) // number
    result = [a_list[x:x+splitNumber] for x in
              range(0, len(a_list), splitNumber)]
    if(len(result) > number):
        result[len(result) - 2] = \
            result[len(result) - 2] + result[len(result) - 1]
        result.pop()
    return result


def identify(matrix):
    """ confirm that matrix is a list of lists
    Args:
        matrix ([[list]]): list of lists
    Returns:
        bool: True if matrix is a list of lists
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not matrix:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not measure(matrix):
        raise TypeError("Each row of the \
matrix must have the same size")
    if not all(type(i) in (int, float) for i in matrix[0]):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    return True


def mutate(matrix, div):
    """ Divide element in matrix by div
    Args:
        matrix ([[list]]): list of lists
    Returns:
        matrix: list of lists
    """
    while True:
        try:
            and_done = [round(j / div, 2) for i in matrix for j in i]
        except ZeroDivisionError:
            raise ZeroDivisionError("division by zero")
        else:
            return and_done


def measure(matrix):
    """ confirm that all rows are the same length
    Args:
        matrix ([[list]]): list of lists
    Returns:
        bool: True if all rows are the same length
    """
    looper = iter(matrix)
    measure = len(next(looper))
    if not all(len(lists) == measure for lists in looper):
        return False
    else:
        return True
