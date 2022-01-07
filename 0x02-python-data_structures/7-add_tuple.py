#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]

    my_list = [tuple(iterable) for iterable in (tuple_a, tuple_b)]
    if len(my_list) == 0:
        return ()
    while len(my_list) < 4:

        if len(my_list[0]) > len(my_list[1]):
            my_list[1] = my_list[1] + (0,) * \
                (len(my_list[0]) - len(my_list[1]))

        elif len(my_list[1]) > len(my_list[0]):
            my_list[0] = my_list[0] + (0,) * \
                (len(my_list[1]) - len(my_list[0]))

        sum = (my_list[0][0] + my_list[1][0],
               my_list[0][1] + my_list[1][1])

        return(tuple(sum))
