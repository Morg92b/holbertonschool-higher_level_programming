#!/usr/bin/env python3

class SwimMixin:
    """
    A mixin class that provides swimming functionality.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying functionality.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon that can swim and fly.
    """
    def roar(self):
        print("The dragon roars!")
