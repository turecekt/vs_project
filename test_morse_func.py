"""Module containing functions test_encode and test_decode."""
# importing functions
from .morse_func import encode, decode


# function responsible for testing the encode function
def test_encode():
    """Tests encode function."""
    assert morse_func.encode("ahoj") == ".- .... --- .--- "
    assert morse_func.encode("SOS") == "... --- ... "
    assert morse_func.encode("1231") == ".---- ..--- ...-- .---- "


# function responsible for testing the decode function
def test_decode():
    """Tests decode function."""
    assert morse_func.decode(".- .... --- .---") == "AHOJ"
    assert morse_func.decode("... --- ...") == "SOS"
    assert morse_func.decode(".---- ..--- ...-- .----") == "1231"
