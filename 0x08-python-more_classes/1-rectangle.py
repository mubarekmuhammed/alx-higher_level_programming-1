#!/usr/bin/python3
    """ Defines an empty Rectangle class.
    """
  
  
class Rectangle:
    """ This class represents a rectangle. """

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance.
        
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """Retrieves the width of a rectangle instance."""
        return self.__width
    
    @width.setter
    def width(self, value)
        """Stes the width of the rectangle with the value."""
        
        Args:
            value: value of the width, always positive
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """Retrieves the height of a rectangle instance."""
        return self.__height
        
    @height.setter
    def height(self, value)
        """Sets the height of a rectangle with the value.
        
        Args:
            value: value of the height, must be positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
