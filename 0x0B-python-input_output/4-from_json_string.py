#!/usr/bin/python3
""" A file that contains a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ A a function that returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
