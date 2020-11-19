"""Tests for example."""
from source import incr
from source import decr


def test_incr():
    """Test decrement and increment function number."""
    assert (incr(5) == 6)
    assert (decr(5) == 4)
