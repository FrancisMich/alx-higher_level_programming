#!/usr/bin/python3
"""Defines the locked class"""


class LockedClass:
    """
    Prevents the user from instantiating
    except called 'first_name'.
    """

    __slots__ = ["first_name"]
