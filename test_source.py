"""Tests for example."""
from source import incr
from source import decr


def test_incr():
    """Test increment and increment function number."""
    assert (incr(5) == 6)


def test_decr():
    """Test decrement and increment function number."""
    assert (decr(5) == 4)
