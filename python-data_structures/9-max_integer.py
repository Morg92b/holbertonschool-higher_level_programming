#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    new_list = my_list[0]
    for index in my_list:
        if index > new_list:
            new_list = index
    return new_list
