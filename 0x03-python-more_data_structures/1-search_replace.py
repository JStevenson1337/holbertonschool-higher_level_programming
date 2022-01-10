#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Return a new list with the search replaced by the replace.
    """
    new_list = [replace if element == search else element
                for element in my_list]
    return new_list
