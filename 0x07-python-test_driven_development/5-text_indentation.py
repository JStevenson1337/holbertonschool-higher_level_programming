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
    i = 0
    j = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print("")
            i += 1
        else:
            print(text[i], end="")
            i + 1
    print("")
    print("")



# Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

# Prototype: def text_indentation(text):
# text must be a string, otherwise raise a TypeError exception with the message text must be a string
# There should be no space at the beginning or at the end of each printed line
# You are not allowed to import any module
