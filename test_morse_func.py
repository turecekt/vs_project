# importing functions
import morse_func


# function responsible for testing the encode function
def test_encode():
    assert morse_func.encode("ahoj") == ".- .... --- .--- "
    assert morse_func.encode("SOS") == "... --- ... "
    assert morse_func.encode("1231") == ".---- ..--- ...-- .---- "


# function responsible for testing the decode function
def test_decode():
    assert morse_func.decode(".- .... --- .---") == "AHOJ"
    assert morse_func.decode("... --- ...") == "SOS"
    assert morse_func.decode(".---- ..--- ...-- .----") == "1231"
