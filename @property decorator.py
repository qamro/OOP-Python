# @property decorator is used to define a method as a property of a class.
# It allows you to access the method like an attribute, without needing to call it with parentheses.
# This can be useful for creating read-only attributes or for encapsulating logic that should be executed when accessing a value.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)
    
# Example usage:
rect = Rectangle(5, 10)
print(f"Area: {rect.area}")          # Accessing area property
print(f"Perimeter: {rect.perimeter}")  # Accessing perimeter property