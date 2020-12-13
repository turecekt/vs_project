"""Unit tests for the triangle.py module"""

from point import distance
import triangle
import math

def test_is_valid():
    """Unit test for the is_valid function."""
    assert triangle.is_valid(10, 15, 20)
    assert not triangle.is_valid(10, 15, 30)

def test_area():
    """Unit test for the area function."""
    hypotenuse = distance(0, 100, 100, 0)
    area = triangle.area(100, 100, hypotenuse)
    assert math.isclose(5000.0, area)

def test_is_right_angle():
    """Unit test for the is_right_angle function."""
    hypotenuse = distance(0, 100, 100, 0)
    assert triangle.is_right_angle(100, 100, hypotenuse)
    hypotenuse = distance(-20, 100, 200, -30)
    assert triangle.is_right_angle(220, 130, hypotenuse)
    assert not triangle.is_right_angle(50, 85, 100)
