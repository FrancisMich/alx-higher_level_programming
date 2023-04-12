#!/usr/bin/python3
"""Define module only sub class of"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of an inherited class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an inherited instance of a_class, otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
