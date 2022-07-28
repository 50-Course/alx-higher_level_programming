#!/usr/bin/python3

"""
Class Square defines a square object with
a private instance attribute [size]

Args:
    size: Optional[int]

Atrribute size must be an integer.

Usage:
    Instantiate the module in your script.

    ```
    from 2-square import Square

    square = Square(5)
    ```
"""


class Square:
    """
    Returns a python object.
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
