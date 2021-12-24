""".

VARIABLE KEY
'sifra' -> 'ukládá morseovku zpravy'
'desifra' -> 'ukládá dešifrovanou zpravu'
'pismeno' -> 'ukládá morseovku jednoho znaku pro dešifrování'
'i' -> 'počítá mezery v morseovce'
'zprava' -> 'ukládá vstup pro kódování/dekódování'
'PovoleneZnaky' -> 'obsahuje string všech povolených znaků pro vstup'
"""
# Definice povolených znaků
import string
PovoleneZnaky = string.digits + string.ascii_uppercase + ',.?!/-():;&=+−_$@" '

# Slovník znaků morseovky
SLOVNIK = {'A': '.-', 'B': '-...',
           'C': '-.-.', 'D': '-..', 'E': '.',
           'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-',
           'L': '.-..', 'M': '--', 'N': '-.',
           'O': '---', 'P': '.--.', 'Q': '--.-',
           'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--',
           'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....',
           '7': '--...', '8': '---..', '9': '----.',
           '0': '-----', ',': '--..--', '.': '.-.-.-',
           '?': '..--..', '!': '-.-.--', '/': '-..-.',
           '-': '-....-', '(': '-.--.', ')': '-.--.-',
           ':': '---...', ';': '-.-.-.', '&': '.-...',
           '=': '-...-', '+': '.-.-.', '−': '-....-',
           '_': '..--.-', '$': '...-..-', '@': '.--.-.'}


def sifrovat(zprava):
    """Funkce pro šifrování do morseovky."""
    sifra = ''

    # Zkontroluje každý znak ve zprávě
    for znak in zprava:

        # Přeskočení uvozovek.
        if znak in ('"', "'"):
            pass

        elif znak != ' ':

            # Vyhledá ve slovníku překlad znaku
            # do morseovky a uloží ho + mezeru do proměnné.
            # V morseovce musí být za každým
            # znakem mezera.
            sifra += SLOVNIK[znak] + ' '
        else:
            # Přidá další mezeru navíc.
            # 2 se dávají mezi slova.
            sifra += ' '

    return sifra


def desifrovat(zprava):
    """Funkce pro dekódování morseovky."""
    zprava += ' '

    desifra = ''
    pismeno = ''

    # Projde všechny znaky ve zprávě
    for znak in zprava:

        # Přeskočení úvozovek
        if znak in ('"', "'"):
            pass

        # V případě, že není mezera:
        elif (znak != ' '):

            # Proměnná na počítání mezer se vynuluje
            i = 0

            # Ukládání morseovky jednoho znaku
            pismeno += znak

        # V případě mezery:
        else:
            # Počítadlo mezer se zvíší o 1.
            # i = 1 znamená, že v proměnné 'znak' je uložený celý znak
            # připraven na přeložení
            i += 1

            # i = 2 v případě, že byli v morseovce 2 mezery za sebou
            # tzn. mezeru mezi slovy
            if i == 2:
                # Do proměnné se přidá mezera na oddělení slov
                desifra += ' '
            else:
                # Vyhledá ve slovníku překlad znaku
                # z morseovky a uloží ho do proměnné.
                desifra += list(SLOVNIK.keys())[list(SLOVNIK.values())
                                                .index(pismeno)]
                pismeno = ''

    return desifra


def main():
    """Hard-coded driver function to run the program."""
    while True:

        print('\nVstup musí být v úvozovkách a bez diakritiky')
        print('Zadejte vstup:')
        zprava = input()
        zprava = zprava.upper()

        while not all(c in PovoleneZnaky for c in zprava) or zprava[0] != '"':
            print('\nVstup obsahuje nepovolené znaky,'
                  'nebo není v úvozovkách')
            print('Zkuste zadat vstup znovu:')
            zprava = input()
            zprava = zprava.upper()

        print('\nVstup je v pořádku')

        if zprava[1] in ('.', '-'):
            result = desifrovat(zprava)
            print('\nDekódovaná morseovka: ', result)
        else:
            result = sifrovat(zprava)
            print('\nZakódovaná morseovka: ', result)


def test_desifrovat():
    """test1."""
    assert desifrovat('".-"') == "A"


def test_sifrovat():
    """test2."""
    assert sifrovat('"A"') == ".- "


# Executes the main function
if __name__ == '__main__':
    main()
