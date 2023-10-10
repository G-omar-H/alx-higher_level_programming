#!/usr/bin/python3
"""
ALX file I/O learning project
"""


def write_file(filename="", text=""):
    """
    function that open a file for read and write
    args:
        @filname(string): file absolute or relative path
        @text(string): text to write into the file
    """
    with open(filename, "w", encoding="UTF8") as fd:
        lenght = fd.write(text)
    return lenght
