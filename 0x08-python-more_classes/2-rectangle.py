#!/usr/bin/python3
"""
Definimos la clase rectangulo
"""


class Rectangle():
    """Definimos el rectangulo"""

    def __init__(self, width=0, height=0):
        """Inicializamos una instacia de rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho de una instacia de rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Verfiicamos el ancho de una instancia"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtenemos la altura de una instacia de rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Verificams la altura de una instacia"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula el area de una instancea"""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calcula el perimetro de una instancea"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
