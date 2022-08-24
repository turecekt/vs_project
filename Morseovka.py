"""MORSE TRANSLATOR."""

# Definování morseovky
DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}


def zakodovani(text):
    """Funkce pro zakodovani.

    funkce pro rozpoznani znaku
    v retezci. Kazdemu znaku priradi znak,
    ktery je definovan v MORSE_CODE_DICT.
    """ 
    zakodovany_text = ""  # zakodovany text = string
    for pismena in text.upper():
        if pismena != " ":  # kontrola mista
            zakodovany_text += DICT[pismena] + ' '
        else:
            zakodovany_text += " "  # pridani mezery
    return zakodovany_text  # vypis zakodovany text


def dekodovani(text):
    """Funkce pro dekodovani.

    funkce pro rozpoznani kodu
    v retezci. Kazdemu znaku kodu priradi znak,
    ktery je definovany v MORSE_CODE_DICT.
    """   
    global prostor
    text += " "
 
    kod = ""
    normal = ""
    for pismena in text:
        if pismena != " ":  # kontrola mista
            kod += pismena  # ukladani morseovky po znaku
            prostor = 0  # prostor
        else:
            prostor += 1  # pokud je rovno 1 oznacuje pismeno
            if prostor == 2:  # pokud je rovno 2 oznacuje nove slovo
                normal += " "  # pridani mezery
            else:
                normal += \
                    list(DICT.keys())[list(DICT.values()).index(kod)]
                kod = ""
    return normal  # vypis dekodovany text


def main():
    """Funkce spousteni programu.

    uzivatel zada "d" pro dekodovani
    nebo "e" pro zakodovani retezce
    """
    sifrovani = input('Morse Encoder/Decoder\n'
                      ' d for decode \n'
                      ' e for encode \n'
                      'Enter what you want to do: \n')
    if sifrovani == 'e':
        text_k_zakodovani = input('Enter text to encode: \n').upper()
        print(zakodovani(text_k_zakodovani))
    elif sifrovani == 'd':
        text_k_dekodovani = input('Enter text to decode: \n')
        print(dekodovani(text_k_dekodovani))
    else:
        print('Wrong choice...\nExiting...')


if __name__ == '__main__':
    main()


def test_zakodovani01():
    """Test k zakodovani textu."""
    assert zakodovani("test") == "- . ... - "


def test_dekodovani01():
    """Test k dekodovani textu."""
    assert dekodovani("- . ... -") == "TEST"


def test_dekodovani02():
    """Test k dekodovani cisel."""
    assert dekodovani("-----  .----  ..---  ...--  ....-") == "0 1 2 3 4"
