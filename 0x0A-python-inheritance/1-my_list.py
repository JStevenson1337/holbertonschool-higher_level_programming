#!/usr/bim/python3
""" My list class """


class MyList(list):
    """ My list class """
    def print_sorted(self):
        """ Print the list in ascending order """
        print(sorted(self))
