#!/usr/bin/python3

""""creating empty class"""


class Rectangle:
    """"empty class created!"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """defining a class of a rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """"set a vlue to a private instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*self.__width + 2*self.height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(self.__height):
            for z in range(self.__width):
                print('#', end="")
            if x < self.__height - 1:
                print()
        return ""

    def __repr__(self):
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
