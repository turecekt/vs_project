"""Library for morse alphabet."""
morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
                    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--',
                    'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
                    'r': '.-.', 's': '...', 't': '-',
                    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                    '9': '----.', ' ': '/', '': ''}

splitCharacter = ' '
errorMessage = "Morse code is not valid!"


def letter2morse(letter: str) -> str:
    """Commenting letter2morse.

    gives morse code from letters
    """
    return morse[letter]


def morse2letter(mor: str) -> str:
    """Commenting morse2letter.

    gives letters from morse code
    """
    return list(morse.keys())[list(morse.values()).index(mor)]


def text2morse(text: str) -> str:
    """Commenting text2morse.

    gives morse code from text
    """
    text = text.strip()
    letters = list(text.lower())
    morseCode = ""
    for let in letters:
        if let in morse:
            morseCode += letter2morse(let)
            morseCode += splitCharacter
    morseCode = morseCode[:-1]
    return morseCode


def morse2text(morseText: str) -> str:
    """Commenting morse2text.

    gives full sentence from morse code
    """
    arrayMorse = morseText.split(splitCharacter)
    text = ""
    for m in arrayMorse:
        if m in list(morse.values()):
            text += morse2letter(m)
        else:
            text = errorMessage
            break
    return text


def test_letter2morse():
    """Commenting test_letter2morse.

    test function for letter2morse function
    """
    assert letter2morse("a") == '.-'
    assert letter2morse("9") != '---..'
    assert letter2morse("") == ""


def test_morse2letter():
    """Commenting test_morse2letter.

    test function for morse2letter function
    """
    assert morse2letter(".") == "e"
    assert morse2letter(".-") == "a"
    assert morse2letter("/") == " "


def test_text2morse():
    """Commenting test_text2morse.

    test function for text2morse
    """
    assert text2morse("sos") == "... --- ..."
    assert text2morse("jAk se Mas") == ".--- .- -.- / ... . / -- .- ..."
    assert text2morse("as/ss") == ".- ... ... ..."
    assert text2morse("mama.") != "-- .- -- .- ."
    assert text2morse("mama.") == "-- .- -- .-"
    assert text2morse("  s b     ") == "... / -..."


def test_morse2text():
    """Commenting test_morse2text.

    test function for morse2text
    """
    assert morse2text("... --- ...") == "sos"
    assert morse2text(".--. . ... / ... . .-.. / " +
                      "...- . -.") == "pes sel ven"
    assert morse2text("") == ""
    assert morse2text(" ") == ""
    assert morse2text("        ") == ""
    assert morse2text("... a --- / --.") == errorMessage


"""Main method."""
if __name__ == "__main__":
    test_letter2morse()
    test_morse2letter()
    test_text2morse()
    test_morse2text()
