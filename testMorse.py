import Morseovka

def testMorse():


"""
Test 1
Input: "Ahoj"
Output: ".-....---.---"
"""

assert MORSE_CODE_DICT("Ahoj") == ".-....---.---"


def testMorse():


"""
Test 2
Input: "SOS"
Output: "... --- ..."
"""

assert MORSE_CODE_DICT("SOS") == "... --- ..."


def testMorse():

"""
Test 3
Input: "jak se mas?"
Output: ".--- .- -.-  ... .  -- .- ... ..--.. "
"""

assert MORSE_CODE_DICT("mas se?") == "-- .- ...  ... . ..--.."


def testMorse():


"""
Test 4
Input: "-.("
Output: "-....- .-.-.- -.--."
"""

assert MORSE_CODE_DICT("-.(") == "-....- .-.-.- -.--."
