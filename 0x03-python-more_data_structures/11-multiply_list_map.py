#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    ''' Multiplies all items in a list
    '''
    new_list = []
    for item in my_list:
        new_list.append(item * number)
    return new_list
