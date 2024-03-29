#!/usr/bin/python3

"""Defining a Rectangle subclass of Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size):
        """Initializing a new square.
        Args:
            size (int): size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
