"""Morse encoder/decoder tests."""
import morse


def test_morse_enc0():
    """
    Encoding test 0.

    Input: "Ahoj"
    Output: ".- .... --- .---"
    """
    assert morse.morse_code("Ahoj") == ".- .... --- .---"


def test_morse_enc1():
    """
    Encoding test 1.

    Input: "Jak se mas"
    Output: ".--- .- -.- / ... . / -- .- ..."
    """
    assert morse.morse_code("Jak se mas") == ".--- .- -.- / ... . / -- .- ..."


def test_morse_enc2():
    """
    Encoding test 2.

    Input: "abcdefgh"
    Output: ".- -... -.-. -.. . ..-. --. ...."
    """
    assert morse.morse_code("abcdefgh") == ".- -... -.-. -.. . ..-. --. ...."


def test_morse_enc3():
    """
    Encoding test 3.

    Input: "opqrstuv"
    Output: "--- .--. --.- .-. ... - ..- ...-"
    """
    assert morse.morse_code("opqrstuv") == "--- .--. --.- .-. ... - ..- ...-"


def test_morse_enc4():
    """
    Encoding test 4.

    Input: "0 1 2 3 4"
    Output: "----- / .---- / ..--- / ...-- / ....-"
    """
    assert morse.morse_code("0 1 2 3 4") == "----- / .---- / ..--- / ...-- / ....-"


def test_morse_enc5():
    """
    Encoding test 5.

    Input: "5 6 7 8 9"
    Output: "..... / -.... / --... / ---.. / ----."
    """
    assert morse.morse_code("5 6 7 8 9") == "..... / -.... / --... / ---.. / ----."


def test_morse_enc6():
    """
    Encoding test 6.

    Input: "ěščřžý.,"
    Output: "escrzy.,"
    """
    assert morse.morse_code("ěščřžý.,") == ". ... -.-. .-. --.. -.-- .-.-.- --..--"


def test_morse_enc7():
    """
    Encoding test 7.

    Input: "áíéúů=?"
    Output: ".- .. . ..- ..- -...- ..--.."
    """
    assert morse.morse_code("áíéúů=?") == ".- .. . ..- ..- -...- ..--.."


def test_morse_enc8():
    """
    Encoding test 8.

    Input: "ďťňó:@/"
    Output: "-.. - -. --- ---... .--.-. -..-."
    """
    assert morse.morse_code("ďťňó:@/") == "-.. - -. --- ---... .--.-. -..-."


def test_morse_enc9():
    """
    Encoding test 9.

    Input: "wxln-"
    Output: ".-- -..- .-.. -. -....-"
    """
    assert morse.morse_code("wxln-") == ".-- -..- .-.. -. -....-"


def test_morse_dec0():
    """
    Decoding test 0.

    Input: ".- .... --- .---"
    Output: "ahoj"
    """
    assert morse.morse_decode(".- .... --- .---") == "ahoj"


def test_morse_dec1():
    """
    Decoding test 1.

    Input: ".--- .- -.- / ... . / -- .- ..."
    Output: "jak se mas"
    """
    assert morse.morse_decode(".--- .- -.- / ... . / -- .- ...") == "jak se mas"


def test_morse_dec2():
    """
    Decoding test 2.

    Input: ".- -... -.-. -.. . ..-. --. ...."
    Output: "abcdefgh"
    """
    assert morse.morse_decode(".- -... -.-. -.. . ..-. --. ....") == "abcdefgh"


def test_morse_dec3():
    """
    Decoding test 3.

    Input: "--- .--. --.- .-. ... - ..- ...-"
    Output: "opqrstuv"
    """
    assert morse.morse_decode("--- .--. --.- .-. ... - ..- ...-") == "opqrstuv"


def test_morse_dec4():
    """
    Decoding test 4.

    Input: "----- / .---- / ..--- / ...-- / ....-"
    Output: "0 1 2 3 4"
    """
    assert morse.morse_decode("----- / .---- / ..--- / ...-- / ....-") == "0 1 2 3 4"


def test_morse_dec5():
    """
    Decoding test 5.

    Input: "..... / -.... / --... / ---.. / ----."
    Output: "5 6 7 8 9"
    """
    assert morse.morse_decode("..... / -.... / --... / ---.. / ----.") == "5 6 7 8 9"


def test_morse_dec8():
    """
    Decoding test 8.

    Input: "-.. - -. --- ---... .--.-. -..-."
    Output: "dtno:@/"
    """
    assert morse.morse_decode("-.. - -. --- ---... .--.-. -..-.") == "dtno:@/"


def test_morse_dec9():
    """
    Decoding test 9.

    Input: ".-- -..- .-.. -. -....-"
    Output: "wxln-"
    """
    assert morse.morse_decode(".-- -..- .-.. -. -....-") == "wxln-"


def test_morse_dec10():
    """
    Decoding test 10.

    Input: ".. --.. -.-- -...- .-.-.- --..--"
    Output: "izy=.,"
    """
    assert morse.morse_decode(".. --.. -.-- -...- .-.-.- --..--") == "izy=.,"
