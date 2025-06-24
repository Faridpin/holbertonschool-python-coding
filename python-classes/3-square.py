#!/usr/bin/python3
'''This module uses getter and setter'''


class Square:
    ''' Square class '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        print(self.__size)

    @size.setter
    def size(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2
