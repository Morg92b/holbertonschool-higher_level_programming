#!/usr/bin/python3
for index in range(0, 10):
    for index_2 in range(1, 10):
        if index >= index_2:
            continue
        elif index == 8 and index_2 == 9:
            print("{}{}".format(index, index_2))
        else:
            print("{}{}, ".format(index, index_2), end="")
