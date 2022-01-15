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
    try:
        identify(matrix)
        print(identify(matrix))
        measure(matrix)
        print(measure(matrix))
        mutate(matrix, 3)
        print(mutate(matrix, div),len(matrix))
    except:
        pass

def identify(matrix):
    """[sumary]
    Args:
        matrix ([type]): [description]
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not measure(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(i) in (int, float) for i in matrix[0]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return True

def mutate(matrix, div):
    """ Divide element in matrix by div """
    and_done = []
    while True:
        try:
            args = list(len(matrix))
            for i in matrix:
                for j in i:
                    and_done.append(j / div)
            and_done = list(len(len(matrix)))
        

        except ZeroDivisionError:
            return None
        except TypeError:
            return None
        except Exception:
            return None
        else:
            return and_done

def measure(matrix):
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
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix_divided(matrix, 3))
print(matrix)

def identify(matrix):
    """[sumary]
    Args:
        matrix ([type]): [description]
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not measure(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(i) in (int, float) for i in matrix[0]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return True



def mutate(matrix, div):
    """ Divide element in matrix by div """
    and_done = []
    while True:
        try:
            for i in matrix:
                for j in i:
                    and_done.append(j / div)
        except ZeroDivisionError:
            return None
        except TypeError:
            return None
        except Exception:
            return None
        else:
            return and_done





def measure(matrix):
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
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix_divided(matrix, 3))
print(matrix)
