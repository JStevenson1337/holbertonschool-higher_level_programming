#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Returns the elements that are in set_1 but not in set_2
    """
    lambda_set_1 = set(map(lambda x: x, set_1))
    lambda_set_2 = set(map(lambda x: x, set_2))
    return lambda_set_1 | lambda_set_2
