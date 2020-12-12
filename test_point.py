from point import distance
from point import Point

def test_distance():
    assert distance(0, -10, 0, 85) == 95

def test_point_distance():
    point_a = Point(-10, 0)
    point_b = Point(85, 0)
    assert point_a.distance(point_b) == 95

def test_str():
    point_a = Point(85, 5)
    print(point_a)
