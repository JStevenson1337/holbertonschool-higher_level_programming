#!/usr/bin/python3

def uppercase(str):
    i = 0
    temp_str = ""
    while (str[i:]):
        ascii_i = ord(str[i])
        if (ascii_i >= 97) & (ascii_i <= 122):
            temp_str += chr(ascii_i - 32)
        else:
            temp_str += chr(ascii_i)
        i += 1
    print('{}'.format(temp_str))
