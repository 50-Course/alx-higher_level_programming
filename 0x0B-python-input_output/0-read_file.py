#!/usr/bin/python3
"""
file: 0-read_file.py
functions:
-> read_file
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
