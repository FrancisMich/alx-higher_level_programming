#!/usr/bin/python3
"""A class MyList that inherits from list
"""


class MyList(list):
    """assume that all the elements of the
    list will be of type int
    """

    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
