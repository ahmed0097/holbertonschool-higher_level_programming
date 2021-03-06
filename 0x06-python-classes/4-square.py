#!/usr/bin/python3
"""Square Class
This is a square
"""


class Square:
    """Square Class
    Square with size
    """
    def __init__(self, size=0):
        """__init__
        initializing square
        """
        self.__size = size

    def area(self):
        """calculates the area of the Square
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
