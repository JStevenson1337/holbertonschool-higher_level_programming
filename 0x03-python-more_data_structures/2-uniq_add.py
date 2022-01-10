#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Return the sum of all unique elements in the list.
    """
    new_list = [element for element in my_list]
    return sum(set(new_list))
