#!/usr/bin/python3


def my_open(filename):
    """
    Opens a file and returns success or failure
    """
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return False


def my_write(filename, data):
    """
    Writes data to a file
    """
    try:
        with open(filename, 'w') as f:
            f.write(data)
    except FileNotFoundError:
        return False


def my_append(filename, data):
    """
    Appends data to a file
    """
    try:
        with open(filename, 'a') as f:
            f.write(data)
    except FileNotFoundError:
        return False


def my_read(filename):
    """
    Reads data from a file
    """
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return False


def my_readlines(filename):
    """
    Reads data from a file and returns a list
    """
    try:
        with open(filename) as f:
            return f.readlines()
    except FileNotFoundError:
        return False


def my_close(filename):
    """
    Closes a file
    """
    try:
        with open(filename) as f:
            f.close()
    except FileNotFoundError:
        return False
