"""Morseovka testy."""
import Morse_Code


def test_morce_code_1():
    """Koder test1."""
    morse = Morse_Code.morse_code("KONTROLNI TEXT")
    assert morse == "-.- --- -. - .-. --- .-.. -. .. / - . -..- -"


def test_morce_code_2():
    """Koder test2."""
    morse = Morse_Code.morse_code("")
    assert morse == ""


def test_morce_code_3():
    """Koder test3."""
    morse = Morse_Code.morse_code("KOLIKATEHO DNESKA JE? 15.6.2018")
    assert morse == "-.- --- .-.. .. -.- .- - . .... --- /" \
                    " -.. -. . ... -.- .- / .--- . ..--.." \
                    " / .---- ..... .-.-.- -.... .-.-.- " \
                    "..--- ----- .---- ---.."


def test_morce_decode_1():
    """Dekoder test1."""
    morse = Morse_Code.morse_decode("-.- --- -. - .-. --- .-.. -. .. /"
                                    " - . -..- -")
    assert morse == "KONTROLNI TEXT"


def test_morce_decode_2():
    """Dekoder test2."""
    morse = Morse_Code.morse_decode(".-- --- .-- / ... ..- -.-. .... /"
                                    " -- --- .-. ... . / -.-. ---"
                                    " -.. . / ---... -....- -....-"
                                    " -....- -.. / ..--.. ..--.."
                                    " ..--.. / ..- .-- ..-")
    assert morse == "WOW SUCH MORSE CODE :---D ??? UWU"


def test_morce_decode_3():
    """Dekoder test3."""
    morse = Morse_Code.morse_decode("")
    assert morse == ""
