#!/usr/bin/python3
'''This file checks for type and value error'''


class Square:
    ''' Square class '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("Size must be >=0")
        self.__size = size
