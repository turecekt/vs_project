def morse(text):

    morseovka = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..', ' ': '.....'}
    preklad = ''

    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    else:
        return 'Vstupni retezec neni napsan v uvozovkach'

    for x in text:
        x = x.upper()
        key_check = x
        if x == '-' or x == '.':
            continue
        if key_check in morseovka:
            continue
        else:
            return 'Vstupni retezec obsahuje neocekavane znaky'

    if text.startswith('.') or text.startswith('−'):
        morseovka_preklad = dict([(v, k) for k, v in morseovka.items()])
        text = text.split(' ')
        for x in text:
            preklad += morseovka_preklad.get(x)

    else:
        text = text.upper()
        for x in text:
            preklad += morseovka.get(x) + ' '
    return preklad.strip()


# here is the input string
inputstr = '"ahoj"'

print(morse(inputstr))


def test_morse_lower():
    """test text-to-morse function with only lowercase letters"""
    assert morse('"ahoj"') == '.- .... --- .---'


def test_morse_upper():
    """test text-to-morse function with only uppercase letters"""
    assert morse('"AHOJ"') == '.- .... --- .---'


def test_morse_mixed():
    """test text-to-morse function with mixed lowercase and uppercase letters"""
    assert morse('"Ahoj"') == '.- .... --- .---'


def test_morse_unsupported():
    """test text-to-morse function with unsupported chars"""
    assert morse('"123ěšč?!"') == 'Vstupni retezec obsahuje neocekavane znaky'


def test_morse_mixed_unsupported():
    """test text-to-morse function with mixed unsupported chars and supported chars"""
    assert morse('"a1"') == 'Vstupni retezec obsahuje neocekavane znaky'


def test_text():
    """test morse-to-text function"""
    assert morse('".- .... --- .---"') == 'AHOJ'


def test_text_unsupported():
    assert morse('"123"') == 'Vstupni retezec obsahuje neocekavane znaky'


def test_text_mixed_unsupported():
    assert morse('".- .... 123"') == 'Vstupni retezec obsahuje neocekavane znaky'
