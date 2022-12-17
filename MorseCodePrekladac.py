# Morse code Překladač


# Slovník pro překlad do morseovy abecedy
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
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ':': '---...',
    ',': '--..--',
    '=': '-...-',
    '.': '.-.-.-',
    '-': '-....-',
    '+': '.-.-.',
    '?': '..--..',
    '!': '-.-.--',
    '@': '.--.-.',
    ' ': '|',
}

# Záměna hodnot ve slovníku pro překlad z morseovy abecedy
slovnik_naopak = {value: key for key, value in slovnik.items()}


def sifrovani(text):
    # Funkce sifrovani() rozpozná znaky ve vloženém řetězci a každému
    # z nich přiřadí korespondující znak ze slovníku a vrátí řetězec
    # Argumenty:
    #    - retezec - Vstup funkce
    # Vrací:
    #    - string - Výstup funkce

    textSifra = ""
    # Counter funguje jako ověření, zda se jedná o první iteraci
    counter = 1
    for znak in text.upper():
        if counter != 1:
            textSifra += " " + slovnik[znak]
        else:
            # U první iterace se nepřidává mezera
            textSifra += slovnik[znak]
            counter = 0
    counter = 1
    return textSifra


def desifrovani(text):
    # Funkce desifrovani() vrací vstupní řetězec převedený z morseovky.
    # Argumenty:
    #    - retezec - Vstup funkce
    # Vrací:
    #    - string - Výstup funkce
    znaky = text.split()
    # vstup se rozdělí na znaky po jednom a poté je hledá ve slovníku
    textDesifra = []
    # Již dešifrované znaky se ukládají do pole textDesifra

    for i in znaky:
        if i in slovnik_naopak:
            textDesifra.append(slovnik_naopak[i])

    # Vrátí výsledný řetězec
    return "".join(textDesifra)


# vstup od uzivatele:

if __name__ == '__main__':

    a = 1
    while a == 1:
        # Smyčka pro restart programu
        print("\n\t\t Překladač morseovky\n")
        text = input("Zadejte text k překladu z abecedy do morseovky: ")
        vysledek = sifrovani(text.upper())
        print(vysledek)

        text = input("Zadejte text k překladu z morseovky do abecedy: ")
        vysledek = desifrovani(text)
        print(vysledek)
        print("Pro restart stisknětě Enter\n")
        konec = input("Pro ukončení programu, zadejte 'konec'\n")
        # Pokud uživatel zadá do vstupu slovo 'konec', program se ukončí
        if konec == "konec":
            a = 2
            input("Program ukončen \n")

# Pytest pro překlad z abecedy do morseovky


def test_sifrovani():
    # Testování funkce sifrovani() na znaky, speciální znaky a mezery z
    # abecedy do morseovky
    assert sifrovani('AHOJ!') == '.- .... --- .--- -.-.--'
    assert sifrovani('1,2,3') == '.---- --..-- ..--- --..-- ...--'
    assert sifrovani('PE PA PO') == '.--. . | .--. .- | .--. ---'
    assert sifrovani('Male Pismena') == '-- .- .-.. . | .--. .. ... -- . -. .-'

# Pytest pro překlad z morseovky do abecedy


def test_desifrovani():
    # Testování funkce desifrovani() na znaky, speciální znaky a mezery z
    # morseovky do abecedy
    assert desifrovani(
        '-.. --- -... .-. -.-- | -.. . -. ..--..') == 'DOBRY DEN?'
    assert desifrovani(
        '.... --- -. --.. .- -- . -. ..--- ...-- .--.-. ...'
        ' . --.. -. .- -- .-.-.- -.-. --..') == 'HONZAMEN23@SEZNAM.CZ'
    assert desifrovani('-- | . | --.. | . | .-. | -.--') == 'M E Z E R Y'
