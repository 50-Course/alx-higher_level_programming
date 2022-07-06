#!/usr/bin/python3
def no_c(my_string):
    if 'C' or 'c' or 'Cc' in my_string:
        my_string.replace("C", "").replace("c", '')
    return my_string
