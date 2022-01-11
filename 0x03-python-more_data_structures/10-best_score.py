#!/usr/bin/python3


def best_score(a_dictionary):
    ''' Returns the key with the highest value in a dictionary
    '''
    if a_dictionary is None:
        return None
    elif len(a_dictionary) == 0:
        return None
    else:
        return max(a_dictionary, key=lambda x: a_dictionary[x])


def best_lamda(a_dictionary):
    ''' Returns the key with the highest value in a dictionary
    '''
    if a_dictionary is None:
        return None
    elif len(a_dictionary) == 0:
        return None
    else:
        return max(a_dictionary, key=lambda x: a_dictionary[x])
