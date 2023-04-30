"""Modul pro kódování a dekódování Morzeovy abecedy."""
Slovnik = {'A': '.-', 'B': '-...',
           'C': '-.-.', 'D': '-..', 'E': '.',
           'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-',
           'L': '.-..', 'M': '--', 'N': '-.',
           'O': '---', 'P': '.--.', 'Q': '--.-',
           'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--',
           'X': '-..-', 'Y': '-.--', 'Z': '--..',
           ', ': '--..--', '.': '.-.-.-',
           '?': '..--..', '/': '-..-.', '-': '-....-',
           '(': '-.--.', ')': '-.--.-', '0': '-----',
           '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....',
           '7': '--...', '8': '---..', '9': '----.'}


def kod(zprava):
    """Funkce na zakodovani.

    Funkce ktera zakoduje zpravu psanou v latince do morzeovy
    abecedy
    """
    sifra = ''
    for letter in zprava:
        if letter != ' ':
            sifra += Slovnik[letter] + ' '
        else:
            sifra += ' '
    return sifra


def dekod(zprava):
    """Funkce na dekodovani.

    Funkce ktera rozlusti zpravu psanou v morzeove
    abecede do latinky
    """
    zprava += ' '

    rozsifra = ''
    jedenznak = ''
    for letter in zprava:

        if (letter != ' '):

            i = 0

            jedenznak += letter

        else:
            i += 1

            if i == 2:

                rozsifra += ' '
            else:

                rozsifra += list(Slovnik.keys())[list(Slovnik.values())
                                                 .index(jedenznak)]
                jedenznak = ''

    return rozsifra


def main():
    """Hlavní blok programu.

    Main, kde program pozna, zda-li je zadana zprava psana v morzeove abecede
    ci latince a spusti spravny kod na prevedeni do druhe abecedy
    """
    zprava = "AHOJ SVETE."
    if ('.' in zprava[0:1] or '-' in zprava[0:1]):
        vyslednazprava = dekod(zprava)
    else:
        vyslednazprava = kod(zprava.upper())

    print(vyslednazprava)


"""Spusti main"""

if __name__ == '__main__':
    main()
