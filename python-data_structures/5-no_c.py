#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for index in my_string:
        if index != "c" and index != "C":
            new_string += index
    return new_string
