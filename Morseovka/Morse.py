"""Importy."""
import collections

"""Zdroj hodnot."""
knihovnaZnaku = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                 '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
                 '.': '.-.-.-', '?': '..--..', '(': '-.--.', ')': '-.--.-',
                 '/': '-..-.', '-': '-....-'}   # Knihovna znaků


def zasifruj(zprava):
    """Šifruje.

    >>> zasifruj('TEST')
    '- . ... - '
    """
    # proměná pro zašifrovanou zprávu
    sifra = ''
    # for postupně vybere každý znak ze zprávy
    for znak in zprava:
        if znak != ' ':
            # pokud je znak z knihovny - přiřadí znak z morseovy abecedy
            # a přidá za něj mezeru
            sifra += knihovnaZnaku[znak] + ' '
        else:
            # pokud je znak mezera - zapíše mezeru
            sifra += ' '
    # vrací zašifrovanou zprávu
    return sifra


def test_sifovani():    # Unit test metody zasifruj()
    """Unit test pro šifrování."""
    assert zasifruj('TEST') == '- . ... - '


def desifruj(zprava):
    """DeŠifruje.

    >>> desifruj('- . ... -')
    'TEST'
    """
    # přidá za zprávu mezeru pro zpřístupnění posledního znaku
    zprava += ' '
    # proměná pro dešifrovanou zprávu
    desifrovano = ''
    # proměná kam se ukládá jeden znak morseovky
    mznak = ''
    # for postupně vybere každý znak ze zprávy
    for znak in zprava:
        # kontroluje zda je znak mezera
        if (znak != ' '):
            # řeší mezery mezi znaky
            i = 0
            # zapíše znak ze zprávy do znaku morseovky
            mznak += znak
        else:
            # pokud je i = 1 - nový charakter morseovky
            i += 1
            # pokud je i = 2 - nové slovo
            if i == 2:
                # přidá mezeru mezi slova
                desifrovano += ' '
            else:
                # ošetřuje nepovolené znaky
                try:
                    # přiřadí hodnotu morseovky ke znaku abecedy
                    # a zapíše do proměné desifrovano
                    desifrovano += list(knihovnaZnaku.keys())[list(
                        knihovnaZnaku.values()).index(mznak)]
                    # vynuluje znak morseovky
                    mznak = ''
                except ValueError:
                    print('Chyba... nepovolený znak')
                    konec()
    # vrací dešifrovanou zprávu
    return desifrovano


def test_desifovani():  # Unit test metody desifruj()
    """Unit test pro dešifrování."""
    assert desifruj('- . ... -') == 'TEST'


def main():
    """Menu."""
    # dotaz na akci
    dotaz = input('Chcete: \n [1] Zašifrovat zprávu \n [2] Dešifrovat zprávu' +
                  '\n [3] Automatický překlad zprávy (může chybovat) \n ' +
                  '[4] Vypsat knihovnu znaků \n')

    # if ... pro vybrání akce
    if (dotaz == '1' or dotaz == '1.'):
        # spouští šifrování
        zprava = input('Zadejte zprávu, kterou chcete zašifrovat' +
                       '(bez diakritiky): \n')
        vysledek = zasifruj(zprava.upper())
        print('šifruji...\nVýsledek: ' + vysledek)
        konec()
    elif (dotaz == '2' or dotaz == '2.'):
        # spouští dešifrování
        zprava = input('Zadejte zašifrovanou zprávu: \n')
        vysledek = desifruj(zprava)
        print('dešifruji...\nVýsledek: ' + vysledek.lower())
        konec()
    elif (dotaz == '3' or dotaz == '3.'):
        zprava = input('Zadejte zprávu: \n')
        # rozhoduje zda je zpráva zašifrovaná
        if (zprava.startswith('.') or zprava.startswith('-')):
            # spouští dešifrování
            vysledek = desifruj(zprava)
            print("dešifruji...")
            print('Výsledek: ' + vysledek.lower())
            konec()
        else:
            # spouští šifrování
            vysledek = zasifruj(zprava.upper())
            print("šifruji...")
            print('Výsledek: ' + vysledek)
            konec()
    elif (dotaz == '4' or dotaz == '4.'):
        # vypíše knihovnu znaků
        temp = collections.Counter(knihovnaZnaku)
        for z in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.?()/-':
            print(z, ' = ', temp[z], '\t',)
        konec()
    else:
        print('Neplatná hodnota')
        konec()


def konec():
    """Konec.

    Ptá se zda chtějí pokračovat
    Y - spouší znovu main() / N - ukončuje program
    """
    x = input('Chcete pokračovat? [Y]/[N] \n')
    if (x == 'N' or x == 'n'):
        exit(0)
    elif(x == 'Y' or x == 'y'):
        main()
    else:
        print('Chyba...')
        konec()


# Spuštění programu
if __name__ == '__main__':
    main()
