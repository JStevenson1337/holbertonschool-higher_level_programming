#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Returns the elements that are not common between two sets
    """
    lambda_set_diff = \
        set(map(lambda x: x, set_1)) | set(map(lambda x: x, set_2))
    return lambda_set_diff - (set_1 & set_2)
