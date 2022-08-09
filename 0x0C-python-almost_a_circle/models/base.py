#!/usr/bin/python3
"""
Base class for every other classes.
"""


class Base:
    """ Root class for sub-classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Default Constructor. 
        Takes Optional argument id 
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
