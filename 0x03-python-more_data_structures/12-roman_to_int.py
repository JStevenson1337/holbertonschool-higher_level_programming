#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif type(roman_string) != str:
        return 0
    else:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                      'M': 1000}
        roman_list = list(roman_string)
        roman_int = 0
        for i in range(len(roman_list)):
            if i == 0:
                roman_int += roman_dict[roman_list[i]]
            elif roman_dict[roman_list[i]] > roman_dict[roman_list[i - 1]]:
                roman_int += roman_dict[roman_list[i]] - \
                            2 * roman_dict[roman_list[i - 1]]
            else:
                roman_int += roman_dict[roman_list[i]]
        return roman_int
