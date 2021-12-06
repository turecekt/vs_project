"""Testování modulu example."""
import example


def test_is_valid():
    """Test vyhodnocení bodů na jedné přímce jako False."""
    assert example.is_valid([(0, 0), (0, 4), (0, -2)]) is False
    assert example.is_valid([(0, 0), (3, 0), (0, -2)]) is True


def test_side_lengths():
    """Test výpočtu délek stran."""
    assert example.side_lengths([(0, 0), (3, 0), (0, 4)]) == [5, 4, 3]


def test_circumference():
    """Test výpočtu obvodu stran."""
    assert example.circumference([(0, 0), (3, 0), (0, 4)]) == 12


def test_is_right():
    """Test určení pravoúhlého trojuhelníku."""
    assert example.is_right([(0, 0), (3, 0), (0, 4)]) is True
    assert example.is_right([(0, 0), (3, 2), (1, 4)]) is False
