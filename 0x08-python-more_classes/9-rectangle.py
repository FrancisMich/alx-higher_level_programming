#!/usr/bin/python3
""" 
Empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Class rectangle"""
    count = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self._width = width
        self._height = height
        Rectangle.count += 1

    @property
    def width(self):
        """Width
        """
        return self._width

    @property
    def height(self):
        """Height
        """
        return self._height

    @width.setter
    def width(self, value):
        """Width setter
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @height.setter
    def height(self, value):
        """Height setter
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect2 must be an instance of Rectangle")
        return rect1 if rect1.area() >= rect2.area() else rect2

    @classmethod
    def square(cls, side=0):
        return cls(side, side)

    def area(self):
        """ Returns rectangle area"""
        return self._width * self._height

    def perimeter(self):
        """ Returns rectangle perimeter"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """ Returns the rectangle with the character #
        """
        if self._width == 0 or self._height == 0:
            return ""
        return ("\n".join(["".join([str(Rectangle.symbol)
                for i in range(self._width)]) for j in range(self._height)]))

    def __repr__(self):
        """ Returns a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted
        """
        Rectangle.count -= 1
        print("Bye rectangle...")
