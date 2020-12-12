"""Unit testy"""

import main

"""Překlad z Abecedy do Morseovy abecedy"""
def test_translation_from_alphabet_to_morse_code():
    assert main.translation("\"Jmenuji se Martin\"", True) == ".-----.-...-.---.. .... --.-.-.-..-."


"""Překlad z Abecedy do Morseovy abecedy - autobus"""
def test_translation_from_alphabet_to_morse_code_autobus():
    assert main.translation("\"Autobus\"", True) == ".-..------.....-..."


"""Překlad z Abecedy do Morseovy abecedy - SOS"""
def test_translation_from_alphabet_to_morse_code_SOS():
    assert main.translation("\"SOS\"", True) == "...---..."


"""Překlad z Abecedy do Morseovy abecedy - mezery"""
def test_translation_from_alphabet_to_morse_code_white_space():
    assert main.translation("\"  \"", True) == ""


"""Mezera na konci slova"""
def test_white_space_end():
    assert main.translation("\"--|.-|--| |....|.-..|.-|-..  \"", False) == "mam hlad"


"""Mezera na začátku slova"""
def test_white_space_start():
    assert main.translation("\" -|---| |.---|...|.|--| |.---|.-\"", False) == "to jsem ja"


"""Mezera na začátku a konci slova"""
def test_white_space_start_end():
    assert main.translation("\"  .-..|.-|...-|..|-.-.|.| |.-| |-|.-|-...|..-|.-..|.   \"", False) == "lavice a tabule"


"""None string"""
def test_none():
    assert main.translation(None, True) == ""


"""Prázdný string"""
def test_empty_string():
    assert main.translation("", True) == ""


"""Překlad z Morseovy abecedy do Abecedy - SOS"""
def test_translation_from_morse_code_to_alphabet_SOS():
    assert main.translation("\"...|---|...\"", False) == "sos"


"""Překlad z Morseovy abecedy do Abecedy - ahoj jmenuji se martin"""
def test_translation_from_morse_code_to_alphabet():
    assert main.translation("\".-|....|---|.---| |.---|--|.|-.|..-|.---|..| |...|.| |--|.-|.-.|-|..|-.\"",
                            False) == "ahoj jmenuji se martin"


"""Překlad z Morseovy abecedy do Abecedy - autobus"""
def test_translation_from_morse_code_to_alphabet_autobus():
    assert main.translation("\".-|..-|-|---|-...|..-|...\"", False) == "autobus"
