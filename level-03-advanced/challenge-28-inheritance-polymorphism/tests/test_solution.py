import pytest
import math
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import Shape, Circle, Rectangle, Triangle


class TestShape:
    def test_shape_has_color(self):
        class ConcreteShape(Shape):
            def area(self):
                return 1
            def perimeter(self):
                return 1
        s = ConcreteShape("red")
        assert s.color == "red"

    def test_area_raises_not_implemented(self):
        s = Shape("red")
        with pytest.raises(NotImplementedError):
            s.area()

    def test_perimeter_raises_not_implemented(self):
        s = Shape("red")
        with pytest.raises(NotImplementedError):
            s.perimeter()


class TestCircle:
    def test_creates_with_color_and_radius(self):
        c = Circle("red", 5)
        assert c.color == "red"
        assert c.radius == 5

    def test_area(self):
        c = Circle("red", 5)
        assert round(c.area(), 2) == 78.54

    def test_area_radius_one(self):
        c = Circle("blue", 1)
        assert round(c.area(), 5) == round(math.pi, 5)

    def test_perimeter(self):
        c = Circle("red", 5)
        assert round(c.perimeter(), 2) == 31.42

    def test_is_shape_subclass(self):
        c = Circle("red", 5)
        assert isinstance(c, Shape)

    def test_describe(self):
        c = Circle("red", 5)
        desc = c.describe()
        assert "red" in desc
        assert "Circle" in desc
        assert "78.54" in desc


class TestRectangle:
    def test_creates(self):
        r = Rectangle("blue", 4, 6)
        assert r.color == "blue"
        assert r.width == 4
        assert r.height == 6

    def test_area(self):
        assert Rectangle("blue", 4, 6).area() == 24

    def test_perimeter(self):
        assert Rectangle("blue", 4, 6).perimeter() == 20

    def test_square_area(self):
        assert Rectangle("green", 5, 5).area() == 25

    def test_is_shape_subclass(self):
        r = Rectangle("blue", 4, 6)
        assert isinstance(r, Shape)

    def test_describe(self):
        r = Rectangle("blue", 4, 6)
        desc = r.describe()
        assert "blue" in desc
        assert "Rectangle" in desc
        assert "24.00" in desc


class TestTriangle:
    def test_creates(self):
        t = Triangle("green", 3, 4, 5)
        assert t.color == "green"

    def test_area_3_4_5(self):
        t = Triangle("green", 3, 4, 5)
        assert round(t.area(), 1) == 6.0

    def test_perimeter_3_4_5(self):
        t = Triangle("green", 3, 4, 5)
        assert t.perimeter() == 12

    def test_equilateral_area(self):
        t = Triangle("red", 5, 5, 5)
        assert t.area() > 0

    def test_is_shape_subclass(self):
        t = Triangle("green", 3, 4, 5)
        assert isinstance(t, Shape)

    def test_polymorphism(self):
        shapes = [
            Circle("red", 1),
            Rectangle("blue", 2, 3),
            Triangle("green", 3, 4, 5)
        ]
        for shape in shapes:
            assert shape.area() > 0
            assert shape.perimeter() > 0
            assert isinstance(shape.describe(), str)
