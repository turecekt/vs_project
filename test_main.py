"""File for unit testing."""
import main


def test_int_to_roman():
    """This function test output of int_to_roman."""
    assert main.int_to_roman(10) == 'X'


if __name__ == '__main__':
    assert main.int_to_roman(326) == 'CCCXXVI'
    test_int_to_roman()
