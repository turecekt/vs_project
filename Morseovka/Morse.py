"""Importy."""


"""Zdroj hodnot."""
knihovnaZnaku = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                 '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
                 '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                 '(': '-.--.', ')': '-.--.-'}


def zasifruj(zprava):
    """Šifruje."""
    sifra = ''
    for znak in zprava:
        if znak != ' ':
            sifra += knihovnaZnaku[znak] + ' '
        else:
            sifra += ' '

    return sifra


def test_sifovani():
    """Unit test pro šifrování."""
    assert zasifruj('test') == '- . ... -'


def desifruj(zprava):
    """DeŠifruje."""
    zprava += ' '
    desifrovano = ''
    mznak = ''
    for znak in zprava:
        if (znak != ' '):
            i = 0
            mznak += znak
        else:
            i += 1
            if i == 2:
                desifrovano += ' '
            else:
                try:
                    desifrovano += list(knihovnaZnaku.keys())[list(
                        knihovnaZnaku.values()).index(mznak)]
                    mznak = ''
                except ValueError:
                    print('Chyba...')
                    konec()

    return desifrovano


def test_desifovani():
    """Unit test pro dešifrování."""
    assert zasifruj('- . ... -') == 'test'


def konec():
    """Konec."""
    x = input('Chcete pokračovat? [Y]/[N] \n')
    if (x == 'N' or x == 'n'):
        exit(0)
    elif(x == 'Y' or x == 'y'):
        main()
    else:
        print('Chyba...')
        konec()


def main():
    """Menu."""
    otazka = input('Chcete zprávu: \n [1] Zašifrovat \n [2] Dešifrovat' +
                   '\n [3] Rozhodni automaticky (může chybovat) \n')

    if (otazka == '1' or otazka == '1.'):
        zprava = input('Zadejte zprávu, kterou chcete zašifrovat' +
                       '(bez diakritiky): \n')
        vysledek = zasifruj(zprava.upper())
        print('šifruji...\nVýsledek: ' + vysledek)
        konec()
    elif (otazka == '2' or otazka == '2.'):
        zprava = input('Zadejte zašifrovanou zprávu: \n')
        vysledek = desifruj(zprava)
        print('dešifruji...\nVýsledek: ' + vysledek.lower())
        konec()
    elif (otazka == '3' or otazka == '3.'):
        zprava = input('Zadejte zprávu: \n')
        if (zprava.startswith('.') or zprava.startswith('-')):
            vysledek = desifruj(zprava)
            print("dešifruji...")
            print('Výsledek: ' + vysledek)
            konec()
        else:
            vysledek = zasifruj(zprava.upper())
            print("šifruji...")
            print('Výsledek: ' + vysledek)
            konec()
    else:
        print('Neplatná hodnota')
        konec()


main()

test_sifovani()
test_desifovani()
