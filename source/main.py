"""Deklarace seznamů s obsahem abecedy a morseovy abecedy."""
charaktery = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
         "....", "..", ".---", "-.-", ".-..", "--", "-.",
         "---", ".--.", "--.-", ".-.", "...", "-", ".--",
         "...-", ".--", "-..-", "-.--", "--..", ".----",
         "..---", "...--", "....-", ".....", "-....",
         "--...", "---..", "----.", "-----", "/"]


def sifrovani_morse(vstup):
    """
    Funkce pro šifrování do morseovy abecedy.

    Funkce rozdělí vstupní řetězec na list písmen,
    zjistí délku listu a pro každou buňku listu zjistí
    dané číslo buňky v stejného znaku příslušném znakovém listu.
    Funkce dále vytvoří prázdné pole do kterého bude
    postupně ukládat znaky ve stejném poli jako zjištěný znak ze vstupu.
    :param vstup:

    :return morse_string:
    """
    text_retezec = vstup.upper()

    # rozdělení vstupního řetězce na list písmen
    rozdeleny_text = [char for char in text_retezec]

    # Zjištění délku listu
    rozdeleny_text_len = len(rozdeleny_text)

    # For cyklus na převod každého pole listu na index stejného
    # znaku v pole charaktery
    prevedeneMorse = []
    for x in range(rozdeleny_text_len):
        y = charaktery.index(rozdeleny_text[x])
        # a následného uložení hodnoty daného indexu v listu morse
        prevedeneMorse.append(morse[y])

    # Deklarace stringu na ukládání výsledku
    morse_string = ''

    # For cyklus pro ukládání každé části pole do stringu
    for pole in prevedeneMorse:
        morse_string += str(pole)
        morse_string += str(" ")
    print("Výsledek převodu:")
    return morse_string


def desifrovani_morse(vstup):
    """
    Funkce pro dešifrování morseovky na text.

    Funkce používá stejný postup jako funkce
    sifrovani_morse s opačnými listy a nepodstatnýmí změnami
    :param vstup:

    :return text_string:
    """
    morse_retezec = vstup.split()
    rozdeleny_retezec = [element for element in morse_retezec]
    rozdeleny_retezec_len = len(rozdeleny_retezec)

    prevedenyText = []
    for x in range(rozdeleny_retezec_len):
        y = morse.index(rozdeleny_retezec[x])
        prevedenyText.append(charaktery[y])
    text_string = ''

    for pole in prevedenyText:
        text_string += str(pole)
    print("Výsledek převodu:")
    return text_string


"""
Blok pro volbu akce.
"""
if __name__ == '__main__':
    text_vstup = input("Zadejte text na převedení:\n")
    vyberAkce = input("Vyberte akci:\n1 - Šifrování do Morseovky "
                      "\n2 - Dešifrování z morseovky\n")

    if vyberAkce == "1":
        print(sifrovani_morse(text_vstup))

    elif vyberAkce == "2":
        print(desifrovani_morse(text_vstup))

    else:
        print("Nesprávná akce")

    input("Stiskněte jakoukoliv klávesu na ukončení programu.")
