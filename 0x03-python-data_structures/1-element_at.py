#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Recieves an element from a list. If idx is negative, return None.
    If out of range, such that idx > my_list return None.
    """
    
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return my_list[idx]
