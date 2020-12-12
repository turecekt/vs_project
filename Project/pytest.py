"""This module tests morsecode."""
import morsecode


def test_simple_input():
    """Tests simple unput."""
    assert morsecode.encode_morse("e", True) == "."
