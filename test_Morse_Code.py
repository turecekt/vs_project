"""Unit testy pro program Morse_code.py."""
import Morse_Code


def test_morse_code_1():
    """Koder test1."""
    morse = Morse_Code.morse_code("KONTROLNI TEXT")
    assert morse == "-.- --- -. - .-. --- .-.. -. .. / - . -..- -"


def test_morse_code_2():
    """Koder test2."""
    morse = Morse_Code.morse_code("")
    assert morse == ""


def test_morse_code_3():
    """Koder test3."""
    morse = Morse_Code.morse_code("KOLIKATEHO DNESKA JE? 15.6.2018")
    assert morse == "-.- --- .-.. .. -.- .- - . .... --- /" \
                    " -.. -. . ... -.- .- / .--- . ..--.." \
                    " / .---- ..... .-.-.- -.... .-.-.- " \
                    "..--- ----- .---- ---.."


def test_morse_code_4():
    """Koder test negativní."""
    morse = Morse_Code.morse_code("KEBABTULE S CHILLI")
    assert not morse == ".---. ..--- .-.- ..-- --..-"


def test_morse_decode_1():
    """Dekoder test1."""
    morse = Morse_Code.morse_decode("-.- --- -. - .-. --- .-.. -. .. /"
                                    " - . -..- -")
    assert morse == "KONTROLNI TEXT"


def test_morse_decode_2():
    """Dekoder test2."""
    morse = Morse_Code.morse_decode(".-- --- .-- / ... ..- -.-. .... /"
                                    " -- --- .-. ... . / -.-. ---"
                                    " -.. . / ---... -....- -....-"
                                    " -....- -.. / ..--.. ..--.."
                                    " ..--.. / ..- .-- ..-")
    assert morse == "WOW SUCH MORSE CODE :---D ??? UWU"


def test_morse_decode_3():
    """Dekoder test3."""
    morse = Morse_Code.morse_decode("")
    assert morse == ""


def test_morse_decode_4():
    """Dekoder test negativní."""
    morse = Morse_Code.morse_decode("-.- -.- -.-")
    assert not morse == "K K K"
