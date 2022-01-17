#!/usr/bin/python3
""" Write a function that prints a \
    text with 2 new lines after \
    each of these characters: ., ? and : """


def text_indentation(text):
    """ Write a function that prints stuff

    Args:  text (str): text to print
    """
    if type(text) is not str or text == "":
        raise TypeError("text must be a string")
    spec_char = [".", "?", ":"]
    while True:
        for ltr in text:
            if ltr in spec_char:
                print(ltr)
                print()
                print('', end="", flush=True)

            else:
                print(ltr, end="", flush=True)
        break
