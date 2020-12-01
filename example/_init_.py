"""Převodník morseové soustavy."""

Znaky = {
    # Abeceda
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
    # Čísla
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
    # Speciální znaky
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    "Ě": "",
    "Š": "",
    "Č": "",
    "Ř": "",
    "Ž": "",
    "Ý": "",
    "Á": "",
    "Í": "",
    "É": "",
    "Ú": "",
    "Ť": "",
}


def encrypt(zprava):
    """Vrací zadanou zprávu převedenou do morseovi abecedy.

    Arguments:
    zprava - text určený k převodu do morseovy soustavy
    Returns:
    sifra - text přeložený do morseovy soustavy
    """
    zprava = zprava.upper()
    sifra = ''

    if zprava == "":
        return "Chyba: prázdné pole"

    for pole in zprava:
        if pole != ' ':
            sifra += Znaky[pole] + ' '
        else:
            sifra += ' '
    return sifra


def decrypt(zprava):
    """Vrací přeložený text z morseovy soustavy.

    Arguments:
    zprava - morseova soustava určená k převodu do textu
    Returns:
    vystup - morseova soustava přeložená do textu
    """
    zprava += ' '
    vystup = ''
    znak = ''

    if zprava == " ":
        return "Chyba: prázdné pole"

    for pole in zprava:
        if(pole != '-' and pole != '.' and pole != ' '):
            vystup = 'špatný formát zadávání'
            return vystup

    for pole in zprava:
        if (pole != ' '):
            i = 0
            znak += pole
        else:
            i += 1
            if i == 2:
                vystup += ' '
            else:
                vystup += list(Znaky.keys())[list(Znaky.values()).index(znak)]
                znak = ''
    return vystup


def choice(vyber):
    """Vrací definici dle zadaného parametru.

    Arguments:
        vyber - hodnota určující volání definice

    Returns:
        result - vrací hodnotu zvolené definice
    """
    if vyber == 1:
        result = encrypt('test')

    elif vyber == 2:
        result = decrypt('- . ... -')

    else:
        result = 'špatný formát zadávání'

    return result


def main():
    """Volání definice v parametru."""
    volani = choice(2)
    print(volani)


if __name__ == '__main__':
    main()


def test_decrypt():
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("- . ... -") == "TEST"
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("..--- -----") == "20"
    """Otestuje zda funkce překládá znaky mimo morseovu abecedu."""
    assert decrypt("AWEGWRHGWRh") == "Špatný formát zadávání"
    """Otestuje zda funkce pracuje s prázdným parametrem."""
    assert decrypt("") == "Chyba: prázdné pole"
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("- . ... - .---- ..--- .--.-.") == "TEST12@"


def test_encrypt():
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test") == "- . ... - "
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("20") == "..--- ----- "
    """Otestuje zda funkce pracuje s prázdným parametrem."""
    assert encrypt("") == "Chyba: prázdné pole"
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test12@") == "- . ... - .---- ..--- .--.-. "


def test_choice():
    """Ověření parametru pro volání definicí."""
    assert choice(0) == "Špatný formát zadávání"
