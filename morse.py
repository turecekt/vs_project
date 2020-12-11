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
    for znak in text.upper():
        if znak != " ":
            sifrovany_text = sifrovany_text + slovnik.get(znak) + " "
        else:
            sifrovany_text += " "
    return(sifrovany_text)


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


# vstup od uzivatele:


def main():
    """Funkce na spousteni programu.

    uzivatel zada textovy retezec
    vypise prelozene textove retezce
    """
    print("\n\t\t PREKLADAC MORSEOVKY")
    text = input("Vlozte text k sifrovani:")
    vysledek = sifrovani(text.upper())
    print(vysledek)

    text = input("Vlozte kod k desifrovani:")
    vysledek = desifrovani(text)
    print(vysledek)


if __name__ == '__main__':
    main()
