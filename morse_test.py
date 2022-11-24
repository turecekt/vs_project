"""Tool for testing morse.py."""
from morse import encode, decode, mainMenu


def test_encode():
    """Testing encoding."""
    assert encode("A") == ".-/"
    assert encode("B") == "-.../"
    assert encode("C") == "-.-./"
    assert encode("D") == "-../"
    assert encode("E") == "./"


def test_decode():
    """Testing decoding."""
    assert decode("..-.") == "F"
    assert decode("--.") == "G"
    assert decode("....") == "H"
    assert decode("..") == "I"
    assert decode(".---") == "J"


def test_mainMenu():
    """Testing menu input."""
    assert mainMenu(1) == 1
    assert mainMenu(2) == 2
    assert mainMenu(3) == 3
