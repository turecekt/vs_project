"""File for unit testing."""
import main


def test_int_to_roman():
    """This function tests output of int_to_roman."""
    assert main.int_to_roman(10) == 'X'
    assert main.int_to_roman(326) == 'CCCXXVI'
    assert main.int_to_roman(111) == 'CXI'
    assert main.int_to_roman(38) == 'XXXVIII'
    assert main.int_to_roman(987) == 'CMLXXXVII'
    assert main.int_to_roman(326) == 'CCCXXVI'
