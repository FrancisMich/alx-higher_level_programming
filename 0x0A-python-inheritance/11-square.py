#!/usr/bin/python3
""" a class Square that inherits from Rectangle 9-rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing the square."""

    def __init__(self, size):
        """Initializing the new square.
        Args:
            size (int): The size of a new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
