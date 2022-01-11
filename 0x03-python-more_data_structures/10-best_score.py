#!/usr/bin/python3


def best_score(a_dictionary):
    ''' Returns the key with the highest value in a dictionary
    '''
    if a_dictionary is None:
        return None
    else:
        best_key = ""
        best_value = 0
        for key, value in a_dictionary.items():
            if value > best_value:
                best_key = key
                best_value = value
        return best_key
