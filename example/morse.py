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
    "Ť": ""
}


def encrypt(zprava):
    """Vrací zadanou zprávu převedenou do morseovi abecedy.

    Arguments:
    zprava - text určený k převodu do morseovy soustavy
    Returns:
    sifra - text přeložený do morseovy soustavy
    """
    if not isinstance(zprava, str):
        return "Parameter musí být (str)"

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
    if not isinstance(zprava, str):
        return "Parameter musí být (str)"

    zprava += ' '
    vystup = ''
    znak = ''

    if zprava == " ":
        return "Chyba: prázdné pole"

    for pole in zprava:
        if(pole != '-' and pole != '.' and pole != ' '):
            vystup = 'Špatný formát zadávání'
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
    if not isinstance(vyber, int):
        return "Parametr musí být (int)"
    if vyber < 0:
        return "Parametr nesmí být záporný"

    if vyber == 1:
        result = encrypt("TEST")

    elif vyber == 2:
        result = decrypt('- . ... -')

    else:
        result = 'Špatný formát zadávání'

    return result


def main():
    """Volání definice v parametru."""
    volani = choice(1)
    print(volani)


if __name__ == '__main__':
    main()
