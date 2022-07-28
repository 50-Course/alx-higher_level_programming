#!/usr/bin/python3

"""
Displays the ful name of a user.
"""

def say_my_name(first_name, last_name=""):
    """
    Concate and return a full name.

    Args:
        first_name: string
        last_name: string

    Raises:
        TypeError

    Returns:
        result: string
    """
    if not isinstance(first_name, str)):
        raises TypeError("first_name must be a string")
    if not isinstance(last_name, str)):
        raises TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

