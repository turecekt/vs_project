import main


def test_translation_from_alphabet_to_morse_code():
    assert main.translation("\"Jmenuji se Martin\"", True) == ".-----.-...-.---.. .... --.-.-.-..-."


def test_translation_from_alphabet_to_morse_code_SOS():
    assert main.translation("\"SOS\"", True) == "...---..."


def test_translation_from_alphabet_to_morse_code_null():
    assert main.translation(None, True) == ""


def test_translation_from_alphabet_to_morse_code_empty_string():
    assert main.translation("", True) == ""


def test_translation_from_morse_code_to_alphabet_null():
    assert main.translation(None, False) == ""


def test_translation_from_morse_code_to_alphabet_empty_string():
    assert main.translation("", False) == ""


def test_translation_from_morse_code_to_alphabet_SOS():
    assert main.translation("\"...|---|...\"", False) == "sos"


def test_translation_from_morse_code_to_alphabet():
    assert main.translation("\".-|....|---|.---| |.---|--|.|-.|..-|.---|..| |...|.| |--|.-|.-.|-|..|-.\"",
                            False) == "ahoj jmenuji se martin"
