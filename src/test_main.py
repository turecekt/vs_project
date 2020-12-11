import main


def test_translation_from_alphabet_to_morse_code():
    assert main.translation("\"Jmenuji se Martin\"", True) == ".-----.-...-.---.. .... --.-.-.-..-."


def test_translation_from_alphabet_to_morse_code_autobus():
    assert main.translation("\"Autobus\"", True) == ".-..------.....-..."


def test_translation_from_alphabet_to_morse_code_SOS():
    assert main.translation("\"SOS\"", True) == "...---..."


def test_translation_from_alphabet_to_morse_code_white_space():
    assert main.translation("\"  \"", True) == ""


def test_white_space_end():
    assert main.translation("\"--|.-|--| |....|.-..|.-|-..  \"", False) == "mam hlad"


def test_white_space_start():
    assert main.translation("\" -|---| |.---|...|.|--| |.---|.-\"", False) == "to jsem ja"


def test_white_space_start_end():
    assert main.translation("\"  .-..|.-|...-|..|-.-.|.| |.-| |-|.-|-...|..-|.-..|.   \"", False) == "lavice a tabule"


def test_null():
    assert main.translation(None, True) == ""


def test_translation_from_alphabet_to_morse_code_empty_string():
    assert main.translation("", True) == ""


def test_translation_from_morse_code_to_alphabet_empty_string():
    assert main.translation("", False) == ""


def test_translation_from_morse_code_to_alphabet_white_space():
    assert main.translation("\"   \"", False) == ""


def test_translation_from_morse_code_to_alphabet_SOS():
    assert main.translation("\"...|---|...\"", False) == "sos"


def test_translation_from_morse_code_to_alphabet():
    assert main.translation("\".-|....|---|.---| |.---|--|.|-.|..-|.---|..| |...|.| |--|.-|.-.|-|..|-.\"",
                            False) == "ahoj jmenuji se martin"


def test_translation_from_morse_code_to_alphabet_autobus():
    assert main.translation("\".-|..-|-|---|-...|..-|...\"", False) == "autobus"
