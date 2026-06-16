import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius


class TestCelsiusToFahrenheit:
    def test_freezing_point(self):
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self):
        assert celsius_to_fahrenheit(100) == 212.0

    def test_negative_forty(self):
        assert celsius_to_fahrenheit(-40) == -40.0, "At -40, Celsius and Fahrenheit are equal"

    def test_body_temperature(self):
        result = celsius_to_fahrenheit(37)
        assert round(result, 1) == 98.6

    def test_returns_float(self):
        result = celsius_to_fahrenheit(0)
        assert isinstance(result, float)


class TestFahrenheitToCelsius:
    def test_freezing_point(self):
        result = fahrenheit_to_celsius(32)
        assert round(result, 5) == 0.0

    def test_boiling_point(self):
        result = fahrenheit_to_celsius(212)
        assert round(result, 5) == 100.0

    def test_negative_forty(self):
        result = fahrenheit_to_celsius(-40)
        assert round(result, 5) == -40.0

    def test_body_temperature(self):
        result = fahrenheit_to_celsius(98.6)
        assert round(result, 1) == 37.0

    def test_returns_float(self):
        result = fahrenheit_to_celsius(32)
        assert isinstance(result, float)


class TestCelsiusToKelvin:
    def test_zero_celsius(self):
        assert celsius_to_kelvin(0) == 273.15

    def test_boiling_point(self):
        assert celsius_to_kelvin(100) == 373.15

    def test_absolute_zero(self):
        result = celsius_to_kelvin(-273.15)
        assert round(result, 5) == 0.0

    def test_negative_celsius(self):
        result = celsius_to_kelvin(-10)
        assert result == 263.15


class TestKelvinToCelsius:
    def test_freezing_point(self):
        result = kelvin_to_celsius(273.15)
        assert round(result, 5) == 0.0

    def test_boiling_point(self):
        result = kelvin_to_celsius(373.15)
        assert round(result, 5) == 100.0

    def test_absolute_zero(self):
        result = kelvin_to_celsius(0)
        assert result == -273.15
