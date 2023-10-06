#!/usr/bin/python3
"""azezeeoazeeazeaazeoazozae"""


def text_indentation(text):
    """lazeaeifdçifklooloo"""

    i = 0

    if type(text) != str:
        raise TypeError("text must be a string")

    txt = text + "_"

    while txt[i] == " ":
        i = i + 1

    while(i < len(text)):
        print("{}".format(txt[i]), end="")

        if txt[i] in {':', '.', '?'}:
            print("{}".format("\n"))

            while txt[i + 1] == ' ':
                i = i + 1

        i = i + 1
