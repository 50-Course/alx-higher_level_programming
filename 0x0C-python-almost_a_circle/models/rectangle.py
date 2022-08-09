#!/usr/bin/python3
"""
file: rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """ Geomentry object for rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ default constructor """

        # Instance variables
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width """
        self.__width = value

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x """
        self.__x = value

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y """
        self.__y = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
