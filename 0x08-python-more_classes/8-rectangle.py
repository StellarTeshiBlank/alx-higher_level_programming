#!/usr/bin/python3
"""
This module has a class that defines a Rectangle
"""

class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the instance with width and height

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            int: Rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            value (int): Rectangle width

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            int: Rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            value (int): Rectangle height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int: Rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            int: Rectangle perimeter or 0 if width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using print_symbol

        Returns:
            str: String representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width for _ in range(self.height))

    def __repr__(self):
        """
        Return the string representation of the rectangle

        Returns:
            str: Rectangle string representation
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Print a message when the instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the bigger Rectangle based on area

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle

        Raises:
            TypeError: If either argument is not an instance of Rectangle

        Returns:
            Rectangle: The rectangle with the larger or equal area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
