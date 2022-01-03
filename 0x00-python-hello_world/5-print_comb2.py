#!/usr/bin/python3
'''
Write a program that prints numbers from 0 to 99.

Numbers must be separated by ,, followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
'''
i = 0

while i <= 99:
    if ( i < 99):
        format_i = "{:02d}".format(i)
        print(format_i, end=', ')
    else:
        print(format_i, end='\n')
    i += 1
