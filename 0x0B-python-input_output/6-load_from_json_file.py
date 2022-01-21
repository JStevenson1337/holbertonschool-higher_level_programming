#!/usr/bin/python3
""" Load from JSON file """
import json


def load_from_json_file(filename):
    """ Load from JSON file """
    try:
        with open(filename, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    finally:
        f.close()
