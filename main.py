<<<<<<< HEAD
=======
"""Prekladac morseovky.g"""

slovnik = {
    """pismena"""
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
    """cisla"""
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
    """jine znaky"""
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
>>>>>>> 5240ede310471af32e89514325fc1460559dafb6


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
<<<<<<< HEAD
    sifrovany_text = ""
=======
    """Funkce sifrovani.

    Funkce rozpozna vlozene znaky
    a ty nahradi symboly z morseovky
    funkce vraci text prelozeny do morseovky
    """
    zasifrovany_text = ""
>>>>>>> 5240ede310471af32e89514325fc1460559dafb6
    for znak in text:
        if znak != " ":
            sifrovany_text = sifrovany_text + slovnik.get(znak) + " "
        else:
            sifrovany_text += " "
    return(sifrovany_text)

def test_sifrovani1():
    vstup = "ahoj".upper()
    vystup = sifrovani(vstup)
    ocekavany_vystup = ".- .... --- .--- "
    assert vystup == ocekavany_vystup


def desifrovani(text):
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
                desifrovany_text = desifrovany_text + pismeno[hodnota.index(morse)]
                morse = ""
    return(desifrovany_text)


print("\t\tPREKLADAC MORSEOVKY")
dotaz = input("Stiskni '1' pro sifrovani, '2' pro desifrovani : ")
if dotaz == '1':
    text_pro_prevod = input("Vlozte text, ktery chcete sifrovat : ").upper()
    vysledek = sifrovani(text_pro_prevod)
    print(vysledek)
else:
    text_pro_prevod = input("Vlozte kod, ktery chcete desifrovat : ")
    vysledek = desifrovani(text_pro_prevod)
    print(vysledek)


<<<<<<< HEAD


=======
def main():
    print("PREKLADAC MORSEOVKY")
    dotaz = input("\nStiskni '1' pro sifrovani, '2' pro desifrovani: ").upper()
    if dotaz == '1':
        text_pro_sifru = input("Vlozte text pro sifrovani: ")
        vysledek = sifrovani(text_pro_sifru)
        print(vysledek)
    else:
        text_pro_desifru = input("Vlozte text pro desifrovani: ")
        vysledek = desifrovani(text_pro_desifru)
        print(vysledek)


if __name__ == '__main__':
    main()

>>>>>>> 5240ede310471af32e89514325fc1460559dafb6
