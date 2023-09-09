"""
Sample modified from CS5500, Mike Shah

A rectangle class
Note that there is no constructor or destructor,
so a default one will be created for us.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @abstractmethod
    def area(self):
        pass

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

class Rectangle(Shape):
    def area(self):
        return self.get_width() * self.get_height()

if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Call a member function
    rect.set_width(3)
    rect.set_height(4)

    # Print out the area function
    print("area:", rect.area())
   
