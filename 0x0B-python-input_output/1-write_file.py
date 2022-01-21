#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters
    """
    try:
        with open(filename, encoding='utf-8') as f:
            if type(text) is list:
                for i in text:
                    print(f.write(text), end="")
            else:
                f.write(text)
        return len(text)
    except FileNotFoundError:
        return 0
    finally:
        f.close()
