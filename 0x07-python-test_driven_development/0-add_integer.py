#!/usr/bin/python3
""" Add two integers """


def add_integer(a, b=98):
    """ Add two integers

    Args:
        a (int): [Mandatory int to pass in]
        b (int): [Optional int to pass in]
    Returns:
        int: [Sum of a and b]
    """
    if type(a) is int:
        pass
    elif type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) is int:
        pass
    elif type(b) is float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
