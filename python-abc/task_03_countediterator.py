#!/usr/bin/python3

class CountedIterator:
    """
    An iterator that counts how many items have been iterated over.
    """

    def __init__(self, ite):
        """
        Initializes the iterator and the count.
        """
        self.iterator = iter(ite)
        self.count = 0

    def get_count(self):
        """
        Returns the number of items iterated so far.
        """
        return self.count

    def __next__(self):
        """
        Returns the next item in the iterator and increments the count.
        Raises StopIteration when the iterator is exhausted.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator itself.
        """
        return self
