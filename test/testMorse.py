import Morseovka

def testMorse():
"""
Test 1
Input: "Ahoj"
Output: ".-....---.---"
"""
assert morse.morse_code("Ahoj") == ".-....---.---"

def testMorse():
"""
Test 2
Input: "SOS"
Output: "... --- ..."
"""
assert morse.morse_code("SOS") == "... --- ..."

def testMorse():
"""
Test 3
Input: "jak se mas?"
Output: ".--- .- -.-  ... .  -- .- ... ..--.. "
"""
assert morse.morse_code("jak se mas?") == ".--- .- -.-  ... .  -- .- ... ..--.. "

def testMorse():
"""
Test 4
Input: "-.("
Output: "-....- .-.-.- -.--."
"""
assert morse.morse_code("-.(") == "-....- .-.-.- -.--."
