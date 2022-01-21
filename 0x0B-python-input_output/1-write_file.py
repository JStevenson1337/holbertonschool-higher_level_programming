#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            return f.write(text)
    except FileNotFoundError:
        return 0
    except Exception as e:
        print("Unknown Error: " + str(e))
        return 0
    finally:
        f.close()
