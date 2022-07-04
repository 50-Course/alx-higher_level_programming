#!/usr/bin/python3

def print_list_integer(my_list=[]):
    if isinstance(my_list, list) and my_list is not None:
        for i in range(len(my_list)):
            print("{:d} \n".format(my_list[i]))
