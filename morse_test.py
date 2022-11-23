"""Tool for testing morse.py."""
from morse import encode, decode


def test_encode():
    """Testing encoding."""
    assert encode("A") == ".-/"


def test_decode():
    """Testing decoding."""
    assert decode(".-") == "A"
