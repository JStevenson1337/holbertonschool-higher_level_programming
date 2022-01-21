#!/usr/bin/python3
""" Write a file """


def write_file(filename="", text=""):
    """
        Write a string to a text file (UTF8)
        and return the number of characters
    """
    try:
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(text)
    except IOError:
        pass
    finally:
        return len(text)
        f.close()
