"""Projekt MORSEOVKA.

Zadani
Vytvořte program, který umí kódovat i dekódovat Morseovu abecedu.
VSTUP
Textový řetězec
Bude čistě na řešitelském týmu, aby vymyslelo vhodný způsob zadávání vstupu.
VÝSTUP
Zakódovaná, případně dekódovaná morseovka
"""


MORSEOVKA = {
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
}


"""Deklarace funkce prevodDoMorseovky s parametrem vstup.
for cyklus pro prochazeni jednotlivych znaku zadaneho vstupniho rezetezce
nacitani znaku do promenne vystup s pripojenim lomitka
(pro lepsi citelnost morseovy abecedy na konzoli)
"""
def prevodDoMorseovky(vstup):
    vystup = ""
    for znak in vstup:
        vystup = vystup + MORSEOVKA[znak] + "/"
    print(vystup)


"""Deklarace funkce prevodZMorseovky s parametrem vstup
pridani mezery na konec vstupniho retezce Morseovy abecedy.
for cyklus pro prochazeni jednotlivych znaku vstupního retezce
pokud nalezne mezeru ulozi do promenne
pokud nalezne 2 po sobe jdouci mezery, prida treti nakonec,
 jakmile nelezne posledni mezeru, jedna se o posledni znak
"""
def prevodZMorseovky(vstup):
    vstup += ' '
    vystup = ''
    pomocna = ''
    for znak in vstup:
        if (znak != ' '):
            i = 0
            pomocna += znak
        else:
            i += 1
            if i == 2:
                vystup += ' '
            else:
                vystup += list(
                    MORSEOVKA.keys())[list(MORSEOVKA.values()).index(pomocna)]
                pomocna = ''
        print(vystup)


"""Unit test pro zakodovani do morseovky
"""
def test_prevodDoMorseovky():
    assert test_prevodDoMorseovky(
        "RADIM13578") == ".-. .- -.. .. -- .---- ...-- ..... --... ---.."


"""Unit test pro dekodovani z morseovky
"""
def test_prevodZMorseovky():
    assert test_prevodZMorseovky(
        ".-. .- -.. .. -- .---- ...-- ..... --... ---..") == "RADIM13578"


"""podminkou if - elif (stisknutim klavesy 1 nebo 2) zakodovat nebo dekodovat
"""
if __name__ == '__main__':
    volba = input("1 pro zakódování, 2 pro dekódování z Morseovy abecedy: ")
    if volba == '1':
        vstup = input("Zadej text pro převod do Morseovy abecedy: ").upper()
        prevodDoMorseovky(vstup)

    elif volba == '2':
        vstup = input("Zadej znaky morseovy abecedy pro převod : ")
        prevodZMorseovky(vstup)

    else:
        print("nezvolil jsi správnou klávesu (1 nebo 2), program končí")
