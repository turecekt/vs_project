"""Prekladac z/do textu do/z kodu morse."""


def texttomorse(text):
    """Prelozeni textu do kodu morse."""
    sp = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
          'f': '..-.',
          'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
          'l': '.-..',
          'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
          'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
          'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
          '.': '.', '-': '-', '1': '.----', '2': '..---', '3': '...--',
          '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
          '9': '----.', '0': '-----', ' ': ' '}
    # vsechny mozne symboly, ktere se mohou zapsat do promenne
    mozne = set('abcdefghijklmnopqrstyuvwxz.1234567890 ')
    stroka = ''
    for i in text:  # kontrola zadaneho textu
        # kontroluje, jestli symbol ze zadaneho textu se lisi
        # od moznych symbolu
        if set(i).difference(mozne):
            print('nespravne znaky')
            stroka = 'nespravne znaky'
            break
        for j in i:  # vypisuje prelozeny text
            print(sp[j], end=" ")
            # zapisuje prelozeny text do promenne
            stroka = stroka + ' ' + sp[j]
        print()
    if stroka == '':  # kontroluje, jestli do stroki je zapsana jenom mezera
        print('prazdne pole')
        return 'prazdne pole'
    else:
        return stroka


def morsetotext(text):
    """Prelozeni z kodu morse do textu."""
    sp = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
          '..-.': 'f',
          '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k',
          '.-..': 'l',
          '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q',
          '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v',
          '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z',
          '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
          '-....': '6', '--...': '7', '---..': '8', '----.': '9',
          '-----': '0', '/': ' '}
    # vsechny mozne symboly, ktere se mohou zapsat do promenne
    mozne = set('.- ')
    stroka = ''
    for j in text:  # kontrola zadaneho textu
        # kontroluje, jestli symbol ze zadaneho textu se lisi
        # od moznych symbolu
        if set(j).difference(mozne):
            print('nespravne znaky')
            stroka = 'nespravne znaky'
            continue
        else:
            # kontroluje, jestli zadany text je v sp
            if set(text).difference(sp):
                print('chyba pri zadavani znaku')
                stroka = 'chyba pri zadavani znaku'
                continue
            else:

                print(sp[j], end=" ")
                stroka = stroka + sp[j]  # zapisuje prelozeny text do promenne
    print()
    if stroka == '':  # kontroluje, jestli do stroki je zapsana jenom mezera
        print('prazdne pole')
        return 'prazdne pole'
    else:
        return stroka


def main():
    """Zadavani textu do jinych funkce."""
    vyber = input('1 - TEXT -> MORSE \n2 - MORSE -> TEXT \n')
    if vyber == str(1):  # kontroluje vyber zadavatele
        text = input("Zapiste vetu:").lower().split()  # zadavani textu
        texttomorse(text)
    elif vyber == str(2):  # kontroluje vyber zadavatele
        text = input("Zapiste Moresouv kod:").lower().split()  # zadavani textu
        morsetotext(text)
    else:  # jestli bude neco jineho, nez 1 a 2
        print("Zvolte prosim 1 nebo 2")


if __name__ == '__main__':
    main()

"""Unittesty."""


# text na Moresuv kod

def test_prelozeni():
    """Test prevodu textu do kodu morse."""
    assert texttomorse("asd") == " .- ... -.."


# Moresuv kod na text

def test_prelozeni1():
    """Test na prelozeni kodu morse do textu."""
    assert morsetotext(['...', '---', '...']) == 'sos'
