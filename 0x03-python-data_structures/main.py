#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

# element_at = __import__('1-element_at').element_at
# idx = 3
# print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

replace_in_list = __import__('2-replace_in_list').replace_in_list
idx = 2
new_element = 15
new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)

# print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer
# print_reversed_list_integer(my_list)
