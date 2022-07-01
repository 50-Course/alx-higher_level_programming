#!/usr/bin/python3

def replace_inline(my_list, idx, new_element):
    """
    Replaces an element of a list at a specific postition. If idx is negative, return None.
    If out of range, such that idx > my_list return None.
    """
    if idx < 0 or len(my_list) < idx:
        return None
    my_list[idx] = new_element
    return my_list


if __name__ == "__main__":
    my_list = [2, 4, 6, 8, 10]
    idx = 3
    new_element = 99
    print(replace_inline(my_list, idx, new_element))
