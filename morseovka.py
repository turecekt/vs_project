# -*- coding: latin-1 -*-
# Morseova abeceda

MORSEOVA_ABECEDA = {
                    ' ': '/', 'A': '.-', 'B': '-...',
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
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', '@': '.--.-.',
                    '  ': '|', '=': '-...-'
                }

def sifrovani():

    text = input('Text pro šifrování do morseovy abecedy: ')
    sifra = [MORSEOVA_ABECEDA[i.upper()] + ' ' for i in text if i.upper()
           in MORSEOVA_ABECEDA.keys()]
    vysledek = ''.join(sifra)
    print(vysledek)


def desifrovani():
 # Dešifrování textu z moreovky
    textNaDesifrovani = input("Text pro dešifrování z morseovy abecedy: ")
    desifra = [j for i in textNaDesifrovani.split()
           for j, k in MORSEOVA_ABECEDA.items() if i == k]
    vysledek = ''.join(desifra)
    print(vysledek)


# Výběrové menu
print('''\n Vyber možnost: 
             1 - Šifrování do morseovy abecedy
             2 - Dešifrování morseovy abecedy
             3 - konec''')



if __name__ == '__main__':
    volba = int(input("Zadej možnost 1-3: "))
    if volba == 1:
        print(sifrovani())
    elif volba == 2:
        print(desifrovani())
    elif volba == 3:
        print("ukončení programu")
    else: 
        print("Špatná možnost, opakuj výběr.")
else:
  print('Znova')
