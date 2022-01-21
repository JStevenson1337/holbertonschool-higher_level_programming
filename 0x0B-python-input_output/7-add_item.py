#!/usr/bin/python3
""" add_item.py: add an item to a list """


import json


def add_item(list_of_items, item_to_add, position):
    """ add_item: add an item to a list """
    list_of_items.insert(position, item_to_add)
    return list_of_items
