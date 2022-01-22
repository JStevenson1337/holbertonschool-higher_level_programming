#!/usr/bin/python3
""" Load from JSON file """
import json


def load_from_json_file(filename):
    """ Load from JSON file """
    with open(filename, "r", encoding="utf-8") as a_file:
        return json.load(a_file)
