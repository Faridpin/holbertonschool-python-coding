#!/usr/bin/python3
""" This module defines a Square class with validation """


class Square:
    """ Square class """

    def __init__(self, size=0):
        self.size = size  # Use the setter to ensure validation

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
