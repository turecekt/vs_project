"""Module containing functions test_encode and test_decode."""
# importing functions
from .morse_func import encode, decode


# function responsible for testing the encode function
def test_encode():
    """Tests encode function."""
    assert encode("ahoj") == ".- .... --- .--- "
    assert encode("SOS") == "... --- ... "
    assert encode("1231") == ".---- ..--- ...-- .---- "


# function responsible for testing the decode function
def test_decode():
    """Tests decode function."""
    assert decode(".- .... --- .---") == "AHOJ"
    assert decode("... --- ...") == "SOS"
    assert decode(".---- ..--- ...-- .----") == "1231"
