#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    result = [t for t in reversed(my_list)]
    for i in result:
        print('{:d}'.format(i), end='\n' if i != result[-1] else '')
