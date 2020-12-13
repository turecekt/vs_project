import unittest

# morseovka
abc = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'ch': '----',
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
    ' ': ' '
}


# kodovaní z abecedy do morseovky
def domorse(preloz):
    zprava = ''  # proměna do ktere budeme dosazovat hodnoty
    # za každe písmeno v preloz se uděla příkaz pod tím.
    # Do proměne zpravy se zapisuje pismeno
    for pismeno in preloz:
        zprava += abc[pismeno] + ' '

    return zprava


# překlad z morseovky do abecedy
def zmorse(preloz):
    # promene

    global i
    preloz += ' '
    slovo = ''
    citext = ''
    for letter in preloz:  # zas loop

        # na rozlišovani nových slov bereme
        if letter != ' ':

            # proměna pro přepinaní
            i = 0

            #
            citext += letter

        # jestli tam nastane mezera
        else:
            # k i se připočte 1 indikuje novou hodnotu
            i += 1

            # jestli i=2 nové slovo
            if i == 2:

                #
                slovo += ' '
            else:

                # k vracene proměne se přípočíta klíč pomocí value
                # kde index hledá tečky čárky
                slovo += list(abc.keys())[list(abc.values()).index(citext)]
                citext = ''

    return slovo


def main():
    moznost = input("Zakodovat(a) přeložit(b)")
    if moznost == "a":
        preloz = input("")
        result = domorse(preloz.lower())
        print(result)
        input("")

    if moznost == "b":
        print("přiklad:.-. .-.. -.-- ")
        preloz = input(" ")
        result = zmorse(preloz)
        print(result.capitalize())
        input("")


if __name__ == '__main__':
    main()
