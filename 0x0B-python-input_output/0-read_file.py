#!/usr/bin/python3

"""
File Reader module.

Usage:
    ```
    from 0-read_file import read_file
    
    file_in = read_file(file_name="")
    ```
"""


def read_file(file_name: str = ""):
    """
    Takes a file argument and prints the
    the result to stdout.

    """
    if file_name is not None:
        try:
            with open(file_name, encoding="utf-8") as f:
                values = f.readlines()
        except (FileNotFoundError):
            pass

        print(values)
