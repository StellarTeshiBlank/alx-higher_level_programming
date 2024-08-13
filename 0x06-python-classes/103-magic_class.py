#!/usr/bin/python3
"""
This is a module that defines a class MagicClass, which stores the properties
of a circumference and calculates its area and perimeter.
"""

import math


class MagicClass:
    """
    A class used to represent a circle and calculate its area and perimeter.

    Attributes
    ----------
    __radius : float
        The radius of the circle (default is 0)
    """

    # Class-level constant to avoid recalculating
    PI = math.pi

    def __init__(self, radius=0):
        """
        Initializes the MagicClass with a radius.

        Parameters
        ----------
        radius : float or int, optional
            The radius of the circle (default is 0)

        Raises
        ------
        TypeError
            If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    @property
    def radius(self):
        """Returns the radius of the circle."""
        return self.__radius

    @property
    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns
        -------
        float
            The area of the circle.
        """
        return self.__radius ** 2 * self.PI

    @property
    def circumference(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.

        Returns
        -------
        float
            The circumference of the circle.
        """
        return 2 * self.PI * self.__radius
