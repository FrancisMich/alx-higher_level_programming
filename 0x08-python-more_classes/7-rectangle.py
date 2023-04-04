#!/usr/bin/python3
""" 
An empty class Rectangle that defines a rectangle
"""

class Rectangle:
    """
    A class that represents a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ 
        Initializes an instance of Rectangle with optional width and height
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ 
        Returns the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """ 
        Returns the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ 
        Sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ 
        Sets the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """ 
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ 
        Returns the perimeter of the rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ 
        Returns a string that represents the rectangle with the print_symbol
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ 
        Returns a string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ 
        Prints a message when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

