"""PREKLADAC MORSEOVKY."""

slovnik = {
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
    '&': ".-...",
    "'": ".----.",
    '@': ".--.-.",
    ')': "-.--.-",
    '(': "-.--.",
    ':': "---...",
    ',': "--..--",
    '=': "-...-",
    '!': "-.-.--",
    '.': ".-.-.-",
    '-': "-....-",
    '+': ".-.-.",
    '"': ".-..-.",
    '?': "..--..",
    '/': "-..-.",
}


def sifrovani(text):
    """Funkce sifrovani.

    funkce rozpozna znaky ve vlozenem
    retezci a kazdemu z nich priradi
    prislusny znak ze slovniku
    return: sifrovany text
    """
    sifrovany_text = ""
    for znak in text:
        if znak != " ":
            sifrovany_text = sifrovany_text + slovnik.get(znak) + " "
        else:
            sifrovany_text += " "
    return(sifrovany_text)


def test_sifrovani():
    """Unit test.

    test na funkci sifrovani()
    """
    ocekavany_vystup = "- . ... - "
    assert sifrovani("TEST") == ocekavany_vystup


def desifrovani(text):
    """Funkce desifrovani.

    funkce rozpozna vlozeny kod v morseovce
    a kazdemu z nich priradi prislusny znak
    ze slovniku
    return: desifrovany text
    """
    text += " "
    pismeno = list(slovnik.keys())
    hodnota = list(slovnik.values())
    morse = ""
    desifrovany_text = ""
    for znak in text:
        if znak != " ":
            morse += znak
            mezery = 0
        else:
            mezery += 1
            if mezery == 2:
                desifrovany_text += " "
            else:
                desifrovany_text += pismeno[hodnota.index(morse)]
                morse = ""
    return(desifrovany_text)


def test_desifrovani():
    """Unit test.

    test na funkci desifrovani()
    """
    vstup = "- . ... -"
    ocekavany_vystup = "TEST"
    assert desifrovani(vstup) == ocekavany_vystup

# vstup od uzivatele:
# do prommene TextSifrovani vlozte text
# do promenne TextDesifrovani vlozte zakodovany text v morseovce


TextSifrovani = "Zde vlozte text".upper()
TextDesifrovani = "- . ... -"

print("\t\t\t PREKLADAC MORSEOVKY")
print('SIFROVANI: ')
print('Vlozili jste: ', TextSifrovani.lower())
print('Vas text v morseovce: ', sifrovani(TextSifrovani))
print('DESIFROVANI: ')
print('Vlozili jste: ', TextDesifrovani)
print('Vas desifrovany text: ', desifrovani(TextDesifrovani))

test_sifrovani()
test_desifrovani()
