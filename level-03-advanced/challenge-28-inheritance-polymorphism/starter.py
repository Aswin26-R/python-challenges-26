import math


class Shape:
    """
    TODO:
    Base class for all shapes. Defines the interface that all shapes must follow.

    The __init__ stores the color.
    The area() and perimeter() methods raise NotImplementedError —
    they MUST be overridden in subclasses.
    The describe() method uses area() and the class name to return a description.
    """

    def __init__(self, color):
        """
        TODO: Store color as self.color
        """
        pass

    def area(self):
        """
        TODO: Raise NotImplementedError.
        This forces subclasses to provide their own implementation.

        raise NotImplementedError("Subclasses must implement area()")
        """
        pass

    def perimeter(self):
        """
        TODO: Raise NotImplementedError.
        """
        pass

    def describe(self):
        """
        TODO:
        Return a string describing the shape.
        Format: "A {color} {ClassName} with area {area:.2f}"

        Example:
            circle = Circle("red", 5)
            circle.describe()  → "A red Circle with area 78.54"

        Hint:
            f"A {self.color} {type(self).__name__} with area {self.area():.2f}"
        """
        pass


class Circle(Shape):
    """
    TODO:
    A circle shape.

    __init__(color, radius):
        Call super().__init__(color) to set the color.
        Store self.radius = radius.

    area(): π × r²  →  math.pi * self.radius ** 2
    perimeter(): 2 × π × r  →  2 * math.pi * self.radius
    """

    def __init__(self, color, radius):
        # TODO: Call super().__init__(color), then store self.radius = radius
        pass

    def area(self):
        # TODO: Return math.pi * self.radius ** 2
        pass

    def perimeter(self):
        # TODO: Return 2 * math.pi * self.radius
        pass


class Rectangle(Shape):
    """
    TODO:
    A rectangle shape.

    __init__(color, width, height):
        Call super().__init__(color).
        Store self.width and self.height.

    area(): width × height
    perimeter(): 2 × (width + height)
    """

    def __init__(self, color, width, height):
        # TODO: Call super().__init__(color), store width and height
        pass

    def area(self):
        # TODO: Return self.width * self.height
        pass

    def perimeter(self):
        # TODO: Return 2 * (self.width + self.height)
        pass


class Triangle(Shape):
    """
    TODO:
    A triangle shape defined by three side lengths a, b, c.

    __init__(color, a, b, c):
        Call super().__init__(color).
        Store self.a, self.b, self.c.

    area(): Use Heron's formula:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    perimeter(): a + b + c
    """

    def __init__(self, color, a, b, c):
        # TODO: Call super().__init__(color), store self.a, self.b, self.c
        pass

    def area(self):
        # TODO: Implement Heron's formula
        pass

    def perimeter(self):
        # TODO: Return self.a + self.b + self.c
        pass
