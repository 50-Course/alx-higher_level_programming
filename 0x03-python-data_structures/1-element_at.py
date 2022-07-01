#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Recieves an element from a list. If idx is negative, return None.
    If out of range, such that idx > my_list return None.
    """
    if idx < 0 or len(my_list) < idx:
        return None
    return my_list[idx]



if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 2
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
