import Morseovka


def test_morse_enc0():
    """
    Encoding Test 0.
    Input:"Ahoj"
    Output:".-....---.---"
    """

    assert Morseovka.MORSE_CODE_DICT("Ahoj") == ".-....---.---"


def test_morse_enc1():
    """
    Encoding Test 1.
    Input:"SOS"
    Output:"... --- ..."
    """
    assert Morseovka.MORSE_CODE_DICT("SOS") == "... --- ..."


def test_morse_enc2():
    """
    Encoding Test 2.
    Input:"jak se mas?"
    Output:".--- .- -.-  ... .  -- .- ... ..--.. "
    """
    assert Morseovka.MORSE_CODE_DICT("mas se?") == "-- .- ...  ... . ..--.."



def test_morse_enc3():
    """
    Encoding Test 3.
    Input:"-.("
    Output:"-....- .-.-.- -.--."
    """
    assert Morseovka.MORSE_CODE_DICT("-.(") == "-....- .-.-.- -.--."