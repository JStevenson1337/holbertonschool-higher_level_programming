#!/usr/bin/python3


def big_diff(my_list=[]):
    if my_list == []:
        return 0

    my_list.sort()
    return my_list[-1] - my_list[0]
