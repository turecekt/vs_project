slovnik = {'A': '.-',
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
    zasifrovany_text = ""
    for znak in text:
        if znak != " ":
            zasifrovany_text = zasifrovany_text + slovnik.get(znak) + " "
        else:
            zasifrovany_text = zasifrovany_text + " "
    return zasifrovany_text


def test_sifrovani():
    ocekavany_vystup = "- . ... - "
    assert sifrovani("TEST") == ocekavany_vystup



def desifrovani(text):
    text = text + " "
    pismena_list = list(slovnik.keys())
    znaky_list = list(slovnik.values())
    morse = ""
    desifrovany_text = ""
    for znak in text:
        if znak != " ":
            morse = morse + znak
            mezera = 0
        else:
            mezera = mezera + 1
            if mezera == 2:
                desifrovany_text = desifrovany_text + " "
            else:
                desifrovany_text = desifrovany_text + pismena_list[znaky_list.index(morse)]
                morse = ""
    return desifrovany_text


def main():
    print("PREKLADAC MORSEOVKY")
    dotaz = input("\nStiskni '1' pro sifrovani, '2' pro desifrovani: ")
    if dotaz == '1':
        text_pro_sifru = input("Vlozte text pro sifrovani: ").upper()
        vysledek = sifrovani(text_pro_sifru)
        print(vysledek)
    else:
        text_pro_desifru = input("Vlozte text pro desifrovani: ")
        vysledek = desifrovani(text_pro_desifru)
        print(vysledek)

test_sifrovani()

if __name__ == '__main__':
    main()
