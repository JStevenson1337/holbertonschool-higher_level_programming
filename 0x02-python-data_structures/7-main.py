#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 2) 
tuple_b = ()
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)


tuple_a = (1, )
tuple_b = (1, )
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
