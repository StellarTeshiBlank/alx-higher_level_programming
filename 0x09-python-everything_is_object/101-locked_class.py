#!/usr/bin/python3
"""
This is a module that contains a class that avoids
dynamically created attributes
"""


class LockedClass:
    """
    This defines a class LockedClass
    """

    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
