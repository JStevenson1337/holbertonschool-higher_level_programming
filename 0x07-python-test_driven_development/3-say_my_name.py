#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """Write a function that prints My name is <first name> <last name>
    Args:
        first_name (str): first name
        last_name (str, optional): lastname . Defaults to "".
    Return:
        None
    """
    while True:
        if is_strings("first_name", first_name) is False:
            raise TypeError("first_name must be a string")
        if is_strings("last_name", last_name) is False:
            raise TypeError("last_name must be a string")
        break
    print("My name is {} {}".format(first_name, last_name))


def is_strings(id, value):
    """ Check if value is a string
    Args:
        id (str): id
        value (str): name of the variable
    Returns:
        bool: True if all strings are strings
    """
    if type(value) is not str:
        return False
    else:
        return True
