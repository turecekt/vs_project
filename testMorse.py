import Morseovka


def testMorse01():
    """
    Test 1
    Input:"Ahoj"
    Output:".-....---.---"
    """

    assert MORSE_CODE_DICT("Ahoj") == ".-....---.---"


def testMorse02():
    """
    Test 2
    Input:"SOS"
    Output:"... --- ..."
    """
    assert MORSE_CODE_DICT("SOS") == "... --- ..."


def testMorse03():
    """
    Test 3
    Input:"jak se mas?"
    Output:".--- .- -.-  ... .  -- .- ... ..--.. "
    """
    assert MORSE_CODE_DICT("mas se?") == "-- .- ...  ... . ..--.."


def testMorse04():
    """
    Test 4
    Input:"-.("
    Output:"-....- .-.-.- -.--."
    """
    assert MORSE_CODE_DICT("-.(") == "-....- .-.-.- -.--."