#!/usr/bin/python3
""" save_to_json_file.py: save to json file """


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters
    """
    try:
        with open(filename, encoding='utf-8') as f:
            if type(text) is list:
                for i in text:
                    f.write(i)
            else:
                print(f.write(text), end="")
        return len(text)
    except IOError:
        return 0
    finally:
        f.close()
