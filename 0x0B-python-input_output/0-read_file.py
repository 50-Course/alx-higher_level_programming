#!/usr/bin/python3

"""
File Reader module.

Usage:
    ```
    from 0-read_file import read_file
    
    file_in = read_file(file_name="")
    ```
"""


def read_file(file_name= ""):
    """
    Takes a file argument and prints the
    the result to stdout.

    """
    with open(file_name, encoding="utf-8") as f:
        values = f.readlines()

    print(values)
