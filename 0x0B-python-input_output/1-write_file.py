#!/usr/bin/python3
'''
file: 3-write_file.py
functions:
-> write_file
'''


def write_file(filename="", text=""):
    ''' writes a string to a text file, returns number of chars written '''

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
