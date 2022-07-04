#!/usr/bin/python3

def print_reversed_list_integer(my_list, idx, new_element):
    """
    Replaces an element of a list at a specific postition. If idx is negative, return None.
    If out of range, such that idx > my_list return None.
    """
    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return None
    my_list[idx] = new_element
    return reversed(my_list)

