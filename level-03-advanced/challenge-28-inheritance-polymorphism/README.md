# Challenge 28: Inheritance and Polymorphism

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 70 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How class inheritance works in Python
- How to call `super().__init__()` to initialize the parent class
- What polymorphism means and how Python achieves it
- How to override methods in a subclass
- Abstract base classes and the concept of interfaces

---

## Problem Description

You will build a simple shape hierarchy. A base `Shape` class defines the interface, and specific shapes (`Circle`, `Rectangle`, `Triangle`) implement it. This models a real-world pattern used in game engines, UI frameworks, and drawing tools.

---

## Requirements

- [ ] `Shape` base class with:
  - `__init__(color)` — stores the color
  - `area()` — raises `NotImplementedError` (must be overridden)
  - `perimeter()` — raises `NotImplementedError` (must be overridden)
  - `describe()` — returns `"A {color} {shape_name} with area {area:.2f}"`

- [ ] `Circle(Shape)` — inherits from `Shape`
  - `__init__(color, radius)`
  - `area()` → `π × r²`
  - `perimeter()` → `2 × π × r`

- [ ] `Rectangle(Shape)` — inherits from `Shape`
  - `__init__(color, width, height)`
  - `area()` → `width × height`
  - `perimeter()` → `2 × (width + height)`

- [ ] `Triangle(Shape)` — inherits from `Shape`
  - `__init__(color, a, b, c)` — three side lengths
  - `area()` → using Heron's formula
  - `perimeter()` → `a + b + c`

---

## Expected Behavior

```python
circle = Circle("red", 5)
circle.area()       # Returns: ~78.54
circle.perimeter()  # Returns: ~31.42
circle.describe()   # Returns: "A red Circle with area 78.54"

rect = Rectangle("blue", 4, 6)
rect.area()         # Returns: 24
rect.perimeter()    # Returns: 20
rect.describe()     # Returns: "A blue Rectangle with area 24.00"

triangle = Triangle("green", 3, 4, 5)
triangle.area()     # Returns: 6.0
triangle.perimeter() # Returns: 12
```

---

## Heron's Formula for Triangle Area

```python
import math
s = (a + b + c) / 2    # semi-perimeter
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
```

---

## How Inheritance Works

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent __init__
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"
```

---

## Hints

> **Hint 1:** Use `super().__init__(color)` in each subclass to call the parent's `__init__`.

> **Hint 2:** `import math` for `math.pi` and `math.sqrt()`.

> **Hint 3:** For `describe()`, get the class name with `type(self).__name__`.

> **Hint 4:** `f"A {self.color} {type(self).__name__} with area {self.area():.2f}"`

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-28-inheritance-polymorphism
pytest tests/ -v
```
