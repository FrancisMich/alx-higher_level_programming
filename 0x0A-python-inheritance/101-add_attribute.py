#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        attr_name (str): The name of the attribute to add to the object.
        attr_value (any): The value of the attribute to add to the object.
    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "dict"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
