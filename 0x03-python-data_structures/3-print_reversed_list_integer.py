#!/usr/bin/python3

def print_reversed(array=[]):
    """
    Prints all integers of a list in reverse order,
    one line at a time.
    """
    if isinstance(array, list) or len(array) != 0:
        reversed_array = reversed(array)
        for i in reversed_array:
            print("{}\n".format(i))




if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reversed_array = print_reversed(my_list)
    print(reversed_array)
