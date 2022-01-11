#!/usr/bin/python3


def weight_average(my_list=[]):
    """Return the average of a list of tuples.
    """
    if my_list is None:
        return None
    elif len(my_list) == 0:
        return None
    else:
        return sum(map(lambda x: x[0] * x[1], my_list)) / sum(map(lambda x: x[1], my_list)
