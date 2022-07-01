#!/usr/bin/python3

def print_list(my_list=[]):
    if isinstance(my_list, list) and my_list is not None:
        for i in my_list:
            if isinstance(i, int):
               print("{} \n".format(i))

if __name__ == "__main__":
    """
    Prints the integers of an array seqeuntially,
    if the array is empty return NOne.
    """
    print_list(my_list=[1, 2, 3, 4, 5])
