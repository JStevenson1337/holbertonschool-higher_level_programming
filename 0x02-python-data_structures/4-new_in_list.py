#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    if element is None:
        return my_list
    else:
        my_new_list = my_list.copy()
        my_new_list.insert(idx, element)
        my_new_list.pop(idx + 1)
        return my_new_list
