#!/usr/bin/python3
"""
test driven devops learning project
python programing language
ALX software engineering

"""


def text_indentation(text):
    """function that prints a text"""

    i = 0

    if type(text) != str:
        raise TypeError("text must be a string")

    txt = text + '_'

    while (txt[i] == " "):
        i += 1

    while (i < len(text)):
        print("{}".format(txt[i]), end="")

        if txt[i] in {':', '.', '?'}:
            print("{}".format("\n"))
            while txt[i + 1] == ' ':
                i += 1
        while txt[i + 1] == ' ':
            i += 1
        i += 1
