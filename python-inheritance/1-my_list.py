#!/usr/bin/python3
"""
Class that extends the built-in list
"""


class MyList(list):
    """
    Prints the list in sorted (ascending) order.
    """
    def print_sorted(self):
        """
    Prints the list elements in ascending order.
        """
        print(sorted(self))
