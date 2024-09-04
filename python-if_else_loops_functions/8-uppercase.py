#!/usr/bin/python3

def uppercase(str):
    for index_char in str:
        if (ord(index_char) <= ord('z') and ord(index_char) >= ord('a')):
            uppercase = chr(ord(index_char) - 32)
        else:
            uppercase = index_char
        print("{}".format(uppercase), end='')
    print()
