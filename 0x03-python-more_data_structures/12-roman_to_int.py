#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string \
    is not isinstance(roman_string, str) \
        | len(roman_string) == 0:
        return 0
    
    while (True):
        if roman_string == "":
            return 0
        elif roman_string[0] == "I":
            return 1 + roman_to_int(roman_string[1:])
        elif roman_string[0] == "V":
            return 5 + roman_to_int(roman_string[1:])
        elif roman_string[0] == "X":
            return 10 + roman_to_int(roman_string[1:])
        elif roman_string[0] == "L":
            return 50 + roman_to_int(roman_string[1:])
        elif roman_string[0] == "C":
            return 100 + roman_to_int(roman_string[1:])
        elif roman_string[0] == "D":
            return 500 + roman_to_int(roman_string[1:])
        elif roman_string[0] == "M":
            return 1000 + roman_to_int(roman_string[1:])
        else:
            return 0
