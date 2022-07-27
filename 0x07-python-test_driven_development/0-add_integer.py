#!/usr/bin/python3
"""
Returns the addition of two integers.

Author: @50-Course (GitHub)
"""

def add_integer(a: int, b: int=98) -> int:
    """
    Returns the result of two inputs, if both
    are either float or integer.
    
    Raises:
        TypeError
    """
    if not (isinstance(a, int) or isinstance(b, int)):
        raise TypeError()
    if type(a) or type(b) == float:
        a = int(a)
        b = int(b)

    return a + b