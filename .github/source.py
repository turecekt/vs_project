"""MORSEOVKA PREKLADAC."""

slovnik = {
    # obsahuje abecedu a znaky
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
    # cisla
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
    # rozne znaky
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


def sifrovany(text):
    """Funkcia sifrovania.
    Rozpozna text a pismena a prelozi ju do morseovky
    return: sifrovany text
    """
    sifrovany_text = ""
    for znak in text.upper():
        if znak != " ":
            # vyhlada znak v kode
            sifrovany_text += slovnik[znak] + ' '
        else:
            # ak najde medzeru vlozi ju tam
            sifrovany_text += " "

    return sifrovany_text


def desifrovany(text):
    """Funkcia desifrovania.
    Rozpozna morseovku a priradi kazdemu znaku, 
    prislusni znak z abecedy(slovniku), 
    return: desifrovany text
    """
    global medzery
    text += " "

    morse = ""
    desifrovany_text = ""
    for znak in text:
        if znak != " ":
            morse += znak
            medzery = 0
        else:
            # 1 medzera = novy znak
            medzery += 1
            if medzery == 2:
                # 2 medzery = nove slovo
                desifrovany_text += " "
            else:
                desifrovany_text += \
                    list(slovnik.keys())[list(slovnik.values()).index(morse)]
                morse = ""
    return desifrovany_text
# vstup od uzivatela:

def main():
    """Funkcia na spustenie programu.
    uzivatel zada text ,
    funkcia vypise preklad 
    """
    print("---- PREKLADAC MORSEOVKY ----")
    """Preklad textu do morseovky"""
    text = input("\n\t\t\t Zadajte text na preklad:")
    vysledok = sifrovany(text.upper())
    print(vysledok)

    text = input("\n\t\t\t Zadajte morseovku na preklad:")
    """Preklad morseovky do textu"""
    vysledok = desifrovany(text)
    print(vysledok)


if __name__ == '__main__':
        main()
