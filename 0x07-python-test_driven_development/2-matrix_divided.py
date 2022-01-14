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
    # with matrix as m:
    #     try:
    #         pass
        
            

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(type(matrix),matrix)
for a_list in matrix:
    print(type(a_list), a_list)
print(type())
print(matrix_divided(matrix, 3))
print(matrix)


# matrix = [
#     [.01, 222, 793],
#     [3, 9, 0]
# ]
# print(matrix_divided(matrix, 3))
# print(matrix)
