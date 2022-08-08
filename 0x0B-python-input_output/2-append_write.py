#!/usr/bin/python3
"""
File: 4-append_write.py
Functions:
 - append_write
"""


def append_write(filename="", text=""):
    """
    Appends a sequence of character to
    the end of a file and return the number
    of characters added.
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
