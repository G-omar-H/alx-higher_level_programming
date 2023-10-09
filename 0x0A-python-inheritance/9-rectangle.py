#!/usr/bin/python3
"""
inheritence alx learning project
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ "
    subclass inheriting from basegeometry class
    """

    def __init__(self, width, height):
        """
        Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of a Rectangle class"""
        return self.__width * self.__height

    def __str__(self):
        """
        custom rectangle reprentation string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
