#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list:
        result = [index for index in reversed(my_list)]
        for i in result:
            print('{:d}'.format(i), end='\n')
    else:
        return None
