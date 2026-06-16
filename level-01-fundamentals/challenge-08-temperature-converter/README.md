# Challenge 08: Temperature Converter

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 25 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to apply mathematical formulas in Python
- Working with floating point numbers
- Rounding numbers with `round()`
- Writing functions that transform values

---

## Problem Description

Temperature can be measured in three scales: Celsius, Fahrenheit, and Kelvin. This challenge requires you to convert between them using the standard formulas.

---

## Requirements

- [ ] `celsius_to_fahrenheit(celsius)` — convert Celsius to Fahrenheit
- [ ] `fahrenheit_to_celsius(fahrenheit)` — convert Fahrenheit to Celsius
- [ ] `celsius_to_kelvin(celsius)` — convert Celsius to Kelvin
- [ ] `kelvin_to_celsius(kelvin)` — convert Kelvin to Celsius

---

## Conversion Formulas

| Conversion | Formula |
|------------|---------|
| Celsius → Fahrenheit | `F = (C × 9/5) + 32` |
| Fahrenheit → Celsius | `C = (F - 32) × 5/9` |
| Celsius → Kelvin | `K = C + 273.15` |
| Kelvin → Celsius | `C = K - 273.15` |

---

## Expected Behavior

```python
celsius_to_fahrenheit(0)
# Returns: 32.0  (freezing point of water)

celsius_to_fahrenheit(100)
# Returns: 212.0  (boiling point of water)

celsius_to_fahrenheit(-40)
# Returns: -40.0  (the point where C and F are equal!)

fahrenheit_to_celsius(32)
# Returns: 0.0

fahrenheit_to_celsius(212)
# Returns: 100.0

celsius_to_kelvin(0)
# Returns: 273.15

celsius_to_kelvin(100)
# Returns: 373.15

kelvin_to_celsius(273.15)
# Returns: 0.0

kelvin_to_celsius(0)
# Returns: -273.15  (absolute zero)
```

---

## About Floating Point Precision

When working with decimals in Python, you may sometimes see results like `100.00000000000001` instead of `100.0`. This is normal floating point behavior.

The tests use `round()` to handle this. Your formulas just need to be correct — precision issues are handled automatically.

---

## Hints

> **Hint 1:** Write out the formula exactly as written: `(celsius * 9/5) + 32`

> **Hint 2:** Python uses `*` for multiplication and `/` for division.

> **Hint 3:** `-40°C` equals `-40°F` — you can use this to verify your formula is correct.

> **Hint 4:** Kelvin has no negative values — the lowest possible temperature is 0K (absolute zero).

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-08-temperature-converter
pytest tests/ -v
```
