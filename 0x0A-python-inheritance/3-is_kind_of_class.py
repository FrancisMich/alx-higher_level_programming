#!/usr/bin/python3
"""Module for checking if an object is an instance or subclass of a given class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object
    is an instance
    of a class that inherited from, the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
