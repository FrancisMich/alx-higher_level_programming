#!/usr/bin/python3
"""A file that returns the dictionary description with a simple
data structure"""


def class_to_json(obj):
    """A function that returns the dictionary descriptio
    with simple data structure."""
    return obj.__dict__
