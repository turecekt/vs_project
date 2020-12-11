"""Testing file for morse."""
from translator import encode, decode


def test_encode():
    """Testing the encode function."""
    assert encode('test') == '- . ... - '


def test_decode():
    """Testing the decode function."""
    assert decode('- . ... - ') == 'test'
