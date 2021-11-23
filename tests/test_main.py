"""Test main skriptu."""

from src.main import jePrvocislo


def test_jePrvocislo():
    """Test funkce jePrvocislo."""
    assert jePrvocislo(9) is False
    assert jePrvocislo(5) is True
