"""Tool for testing morse.py."""
import morse


def test_encode():
    """Testing encoding."""
    assert morse.encode("A") == ".-/"


def test_decode():
    """Testing decoding."""
    assert morse.decode(".-") == "A"
