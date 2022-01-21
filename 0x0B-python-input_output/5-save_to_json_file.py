#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation
    """
    try:
        with open(filename, 'w') as f:
            json.dump(my_obj, f)
    except Exception as e:
        print("can't save object to", filename, e)
    finally:
        f.close()
