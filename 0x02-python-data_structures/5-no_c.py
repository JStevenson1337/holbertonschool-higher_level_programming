#!/usr/bin/python3


def no_c(my_string):
    my_array = []
    for i in my_string:
        if i != 'c' and i != 'C':
            my_array.append(i)
    return ''.join(my_array)
