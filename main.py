
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



MORSE_TO_ALFA = {}
for key, value in Morzeovka.items():
    MORSE_TO_ALFA[value] = key


def alfa_to_morse(sprava):
    """Preklad do morzeovky."""
    morse = []
    for char in sprava:
        if char in Morzeovka:
            morse.append(Morzeovka[char])
    return " ".join(morse)


def morse_to_alfa(sprava):
    """Preklad do alfy."""
    sprava = sprava.split(" ")
    alfa = []
    for code in sprava:
        if code in MORSE_TO_ALFA:
            alfa.append(MORSE_TO_ALFA[code])
    return " ".join(alfa)
