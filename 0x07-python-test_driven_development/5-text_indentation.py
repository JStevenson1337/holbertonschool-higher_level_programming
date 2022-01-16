#!/usr/bin/python3
""" Write a function that prints a text with 2 new lines after each of these characters: ., ? and : """


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
                print("\n\n")
            else:
                print(ltr, end="")
        break




# Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

# Prototype: def text_indentation(text):
# text must be a string, otherwise raise a TypeError exception with the message text must be a string
# There should be no space at the beginning or at the end of each printed line
# You are not allowed to import any module
