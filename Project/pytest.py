import morsecode

def test_simple_input():
    assert morsecode.encode_morse("e", True) == "."

