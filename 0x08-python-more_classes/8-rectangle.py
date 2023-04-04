#!/usr/bin/python3
"""Empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    symbol = "#"

    def __init__(self, w=0, h=0):
        """Instantiation with optional width and height"""
        self.width = w
        self.height = h
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width"""
        return self.__width

    @property
    def height(self):
        """Height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def greater_than_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Return the string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join([str(self.symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye Rectangle...")
