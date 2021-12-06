"""Morse script."""

znaky = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----'
}


def encodovani(vstup):
    """Encode text.

    >>> encodovani('A')
    '.-'
    """
    vstup = vstup.upper()
    zprava = ''
    for znak in vstup:
        if znak != ' ':
            zprava += znaky[znak] + ' '
        else:
            zprava += ' '
    return zprava[:-1]


def decodovani(vstup):
    """Decode text.

    >>> decodovani('.-')
    'A'
    """
    try:
        vstup += " "
        desifrovanaZprava = ''
        pismeno = ''
        i = 0
        for letter in vstup:
            if (letter != ' '):
                i = 0
                pismeno += letter
            else:
                i += 1
                if i == 2:
                    desifrovanaZprava += ' '
                else:
                    desifrovanaZprava += list(znaky.keys())[
                        list(znaky.values()).index(pismeno)
                        ]
                    pismeno = ''
        return desifrovanaZprava
    except ValueError:
        return 0


def vypisZnaku():
    """Write the text.

    >>> vypisZnaku()
    """
    print("Podporované znaky:")
    znakPodporovan = ""
    vypisZnaku = ""
    for znakPodporovan in znaky:
        vypisZnaku += znakPodporovan

    print(vypisZnaku)


def start():
    """Input.

    >>> start()
    """
    print("Zvolte: 'e' pro encode, 'd' pro decode,"
          " jinou klávesu pro ukončení programu:")
    typ = input()

    if typ == "e":
        vypisZnaku()
        print("Zadejte vstup pro encode:")
        vstup = input()
        print("Enkodováno:")
        print(encodovani(vstup))
    elif typ == "d":
        print("Zadejte vstup pro decode:")
        vstup = input()

        res = decodovani(vstup)
        if res != 0:
            print("Dekodováno:")
            print(decodovani(vstup))
        else:
            print("Chyba - Nelze dekódovat.")
            start()


def main():
    """Start program.

    >>> main()
    """
    print("Vítejte v encoderu/decoderu pro morseovku")
    start()


if __name__ == '__main__':
    main()