"""Encoding/decoding morse code to text and vice-versa."""


def morse(text):
    """Decode or encode the text.

    This function takes an input string, decides whether it decodes
    from morse code or encodes text to morse code and executes
    itself accordingly.
    """
    # This dictionary contains the specified letters and
    # their morse code equivalent.
    morseovka = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..', ' ': '.....'}
    preklad = ''

    # If the input string does not start with double quotes,
    # print an error (double quotes were a project requirement).
    # The double quotes are then trimmed for easier work with the string.
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    else:
        return 'Vstupni retezec neni napsan v uvozovkach'

    # Check if the input string contains any letters that are not
    # defined in the dictionary, then print an error.
    for x in text:
        x = x.upper()
        key_check = x
        if x == '-' or x == '.':
            continue
        if key_check in morseovka:
            continue
        else:
            return 'Vstupni retezec obsahuje neocekavane znaky'

    # If the input string starts with a dot or a dash,
    # the program will convert morse code back to text.
    # The string is split if there is a space, and that
    # split string gets converted via the dictionary.
    if text.startswith('.') or text.startswith('−'):
        morseovka_preklad = dict([(v, k) for k, v in morseovka.items()])
        text = text.split(' ')
        for x in text:
            preklad += morseovka_preklad.get(x)

    # Else the program converts text to morse code.
    else:
        text = text.upper()
        for x in text:
            preklad += morseovka.get(x) + ' '
    return preklad.strip()


# Here is the input string, where the user can
# freely input to encode/decode.
inputstr = '"ahoj"'

# Call to method for encoding/decoding with the
# input string as the parameter.
print(morse(inputstr))


# Here are the unit tests.
def test_morse_lower():
    """Test text-to-morse function with only lowercase letters."""
    assert morse('"ahoj"') == '.- .... --- .---'


def test_morse_upper():
    """Test text-to-morse function with only uppercase letters."""
    assert morse('"AHOJ"') == '.- .... --- .---'


def test_morse_mixed():
    """Testing.

    Test text-to-morse function with mixed
    lowercase and uppercase letters.
    """
    assert morse('"Ahoj"') == '.- .... --- .---'


def test_morse_unsupported():
    """Test text-to-morse function with unsupported chars."""
    assert morse('"123ěšč?!"') == 'Vstupni retezec obsahuje neocekavane znaky'


def test_morse_mixed_unsupported():
    """Testing.

    Test text-to-morse function with mixed
    unsupported chars and supported chars.
    """
    assert morse('"a1"') == 'Vstupni retezec obsahuje neocekavane znaky'


def test_text():
    """Test morse-to-text function."""
    assert morse('".- .... --- .---"') == 'AHOJ'


def test_text_unsupported():
    """Test morse-to-text function with unsupported chars."""
    assert morse('"123"') == 'Vstupni retezec obsahuje neocekavane znaky'


def test_text_mixed_unsupported():
    """Testing.

    Test morse-to-text function with mixed
    unsupported chars and supported chars.
    """
    assert morse('".- 123"') == 'Vstupni retezec obsahuje neocekavane znaky'
