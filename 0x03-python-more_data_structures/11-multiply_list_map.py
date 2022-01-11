#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    ''' Multiplies all items in a list
    '''
    new_list = []
    return(list(map(lambda x: x * number, my_list)))
