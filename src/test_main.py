import main

def test_translation_from_alphabet_to_morse_code():
    result = main.translation("Jmenuji se Martin", True)
    assert result == ".-----.-...-.---.. .... --.-.-.-..-."
