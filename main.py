"""Slovnik morseovy abecedy."""
Morzeovka = {'A': '.-',
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
             '0': '-----',
             '1': '.----',
             '2': '..---',
             '3': '...--',
             '4': '....-',
             '5': '.....',
             '6': '-....',
             '7': '--...',
             '8': '---..',
             '9': '----.'}


# Generuje MORSE_TO_ALFA z ALFA_TO_MORSE
MORSE_TO_ALFA = {}
for key, value in Morzeovka.items():
    MORSE_TO_ALFA[value] = key


def alfa_to_morse(sprava):
    """Preklad do morzeovky."""
    morse = []  # Obsahuje morzeovku
    for char in sprava:
        if char in Morzeovka:
            morse.append(Morzeovka[char])
    return " ".join(morse)  # vrací morseovku


def morse_to_alfa(sprava):
    """Preklad do alfy."""
    sprava = sprava.split(" ")
    alfa = []  # Obsahuje alfanumericke znaky
    for code in sprava:
        if code in MORSE_TO_ALFA:
            alfa.append(MORSE_TO_ALFA[code])
    return " ".join(alfa)  # vrací text


# Hlavní funkce pro překlad
def main():
    """Hlavni cast programu."""
    while 1:
        # vybrání programu pro překlad
        vstup = input("Morse => Alfa (1) alebo Alfa to Morse (2)? ").upper()
        if vstup == "1" or vstup == "2":
            break

# program pro překlad z morseovky do textu
    if vstup == "1":
        print("Zadaj kod v morzeovke: ")  # zadání kódu morseovky
        morse = input("> ")
        alfa = morse_to_alfa(morse)
        print(alfa)  # vypsání přeložené morseovky do textu

# program pro překlad z textu do morseovky
    elif vstup == "2":
        print("Zadaj text: ")  # zadání textu
        alfa = input("> ").upper()
        morse = alfa_to_morse(alfa)
        print(morse)  # vypsání přeloženého textu do morseovky


if __name__ == "__main__":
    main()


# testování překladu textu do morseovky
def test_alfa_to_morse():
    """Testovani prekladu alfa to morse."""
    assert alfa_to_morse("SOS") == "... --- ..."


# testování překladu morseovky do textu
def test_morse_to_alfa():
    """Testovani prekladu morse to alfa."""
    assert morse_to_alfa("... --- ...") == "S O S"
