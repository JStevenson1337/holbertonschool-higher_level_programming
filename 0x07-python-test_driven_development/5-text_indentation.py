#!/usr/bin/python3
""" Write a function that prints a \
    text with 2 new lines after \
    each of these characters: ., ? and : """


def text_indentation(text):
    """ [summary]

        Args: text ([type]): [description]
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        raise ValueError("text must not be empty")
    spec_char = [".", "?", ":"]
    while True:
        for ltr in text:
            if ltr in spec_char:
                print(ltr)
                print("")
            else:
                print(ltr, end="")
        break
