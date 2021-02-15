"""Program na přeložení Morseovy abecedy."""

abeceda = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
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

}


# příklady abecedy do morseovky
def domorzeovky(preloz):
    """Přeložení do Morseovy abecedy."""
    zprava = " "
    for pismeno in preloz:

        if pismeno != ' ':

            # podívá se a přidá
            # kód z morseovky
            zprava += abeceda[pismeno] + ' '
        else:
            # 1 indikuje mezeru
            # a 2 indikuje  slova
            zprava += " "
    return zprava


def odmorzeovky(preloz):
    """Přeložení z Morseovy abecedy."""
    global i
    preloz += ' '
    slovo = ''
    x = ''
    for letter in preloz:  # zas loop

        #  bereme na rozlišovani nových slov
        if letter != ' ':

            #  pro přepinaní
            i = 0

            #
            x += letter

        # kdyz tam zustane mezera
        else:
            # u i + 1 ukáže novou hodnotu
            i += 1

            # když i=2 tak bude nové slovo
            if i == 2:

                #
                slovo += ' '
            else:

                # k vracene proměne se přípočíta pomocí value
                # kde se hledá čárky tečky
                slovo += list(abeceda.keys())[list(abeceda.values()).index(x)]
                x = ''

    return slovo


def main():
    """Input charakteru."""
    moznost = input("do morseovky(1) z morseovky(2): ")
    if moznost == "1":
        prelozit = input(" ")
        vysledek = domorzeovky(prelozit.lower())
        print(vysledek)

    if moznost == "2":
        print("přiklad:-.-. .-.. -.- ")
        prelozit = input(" ")
        vysledek = odmorzeovky(prelozit)
        print(vysledek)


if __name__ == '__main__':
    main()
