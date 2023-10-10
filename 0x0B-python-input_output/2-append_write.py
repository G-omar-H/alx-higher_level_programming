#!/usr/bin/python3
"""
ALX file I/O learning project
"""


def append_write(filename="", text=""):
    """
    function that opens a file and append content into it
    args:
        @filname(string): file absolute or relative path
        @text(string): text to apppend into the file
    """
    with open(filename, "a", encoding="UTF8") as fd:
        lenght = fd.write(text)
    return lenght
