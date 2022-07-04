#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    """
    Replaces an element of a list at a specific postition. If idx is negative, return None.
    If out of range, such that idx > my_list return None.
    """
    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return my_list
    my_list[idx] = new_element
    return (my_list)

