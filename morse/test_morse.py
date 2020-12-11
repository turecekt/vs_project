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

    Input: "01234"
    Output: "----- .---- ..--- ...-- ....-"
    """
    assert morse.morse_code("01234") == "----- .---- ..--- ...-- ....-"


def test_morse_enc5():
    """
    Encoding test 5.

    Input: "56789"
    Output: "..... -.... --... ---.. ----."
    """
    assert morse.morse_code("56789") == "..... -.... --... ---.. ----."


def test_morse_enc6():
    """
    Encoding test 6.

    Input: "ěščřž.,"
    Output: ". ... -.-. .-. --.. .-.-.- --..--"
    """
    assert morse.morse_code("ěščřž.,") == ". ... -.-. .-. --.. .-.-.- --..--"


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

    Input: "wxln-ý"
    Output: ".-- -..- .-.. -. -....- -.--"
    """
    assert morse.morse_code("wxln-ý") == ".-- -..- .-.. -. -....- -.--"


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

    Input: ".--- .- -.- ... . -- .- ..."
    Output: "jaksemas"
    """
    assert morse.morse_decode(".--- .- -.- ... . -- .- ...") == "jaksemas"


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

    Input: "----- .---- ..--- ...-- ....-"
    Output: "01234"
    """
    assert morse.morse_decode("----- .---- ..--- ...-- ....-") == "01234"


def test_morse_dec5():
    """
    Decoding test 5.

    Input: "..... -.... --... ---.. ----."
    Output: "56789"
    """
    assert morse.morse_decode("..... -.... --... ---.. ----.") == "56789"


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
