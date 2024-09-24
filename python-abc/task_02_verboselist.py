#!/usr/bin/python3

class VerboseList(list):
    """
    A subclass of the built-in list that provides verbose output
    for certain operations (append, extend, remove, pop).
    """
    def append(self, item):
        """
        Adds an item to the list and prints a message
        """
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, item):
        """
        Extends the list with multiple items and prints a message
        """
        print("Extended the list with [{}] items.".format(len(item)))
        super().extend(item)

    def remove(self, item):
        """
        Removes an item from the list and prints a message
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list and prints a message
        """
        if self:
            pop_item = self[index]
            print("Popped [{}] from the list.".format(pop_item))
            return super().pop(index)
        else:
            raise ValueError("Cannot pop from an empty list.")
