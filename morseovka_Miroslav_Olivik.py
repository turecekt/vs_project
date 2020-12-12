#!/usr/bin/env python 3

"""Jako první věc si musíme definovat abecedu."""


SLOVNIK_MORSEOVKA = {' ': '/', 'A': '.-',
                     'B': '-...', 'C': '-.-.',
                     'D': '-..', 'E': '.',
                     'F': '..-.', 'G': '--.', 'H': '....',
                     'I': '..', 'J': '.---',
                     'K': '-.-', 'L': '.-..',
                     'M': '--', 'N': '-.',
                     'O': '---', 'P': '.--.',
                     'Q': '--.-', 'R': '.-.',
                     'S': '...', 'T': '-',
                     'U': '..-', 'V': '...-',
                     'W': '.--', 'X': '-..-',
                     'Y': '-.--', 'Z': '--..',
                     '1': '.----', '2': '..---',
                     '3': '...--', '4': '....-',
                     '5': '.....', '6': '-....',
                     '7': '--...', '8': '---..',
                     '9': '----.', '0': '-----',
                     ',': '--..--', '.': '.-.-.-',
                     '?': '..--..', '/': '-..-.', '-': '-....-',
                     '(': '-.--.', ')': '-.--.-'}

"""Dále definujeme první funkci."""
"""Jako první věc definujeme text, kterému máme doplnit text pro kodovani."""
"""Dále vytvoříme převodový text na kod."""
"""Vytvoříme string k danemu code."""
"""A string necháme přečíst."""


def Text_To_Code(): """Funkce - překlad slov do morseovky."""
text2 = input("Napište slova, která chcete kodovat: ")
code2 = [SLOVNIK_MORSEOVKA
        [i.upper()] + " "
         for i in text2 if i.upper() in SLOVNIK_MORSEOVKA.keys()]
morseovka = "".join(code2)
print(morseovka)


"""Stejný způsob použijeme i zde u dekodovani námi zadaného textu."""
"""Vytvoříme zde to, že námi zadaný kod program rozloží na jednotky."""
"""Opet nechame udělat string z code a necháme ho vypsat."""


def Code_To_Text(): """Vytvořené funkce - přeložení morseovk."""


text1 = input("Napište kod, který chcete dekodovat: ")
code1 = [k for i in text1.split() for k,
         v in SLOVNIK_MORSEOVKA.items() if i == v]
novytext = "".join(code1)
print(novytext)


"""Vypiseme menu pro vyber, co hceme aby program delal."""
"""Na zaver vypisime cyklus, ktery nám k menu ve stringu priradi i funkce."""
"""Zvolili jsme fci else, která nám pokryje jinou možnost než-li 1-3."""


print("""\n1 - TEXT KE KODOVÁNÍ \n2 - KÓD K ROZKÓDOVÁNÍ\n3 - KONEC\n""")

if __name__ == '__main__':

    while True:

        vyber = int(input("TVŮJ VÝBĚR: "))
        if vyber == 1:
            print(Text_To_Code())
            break

        elif vyber == 2:
            print(Code_To_Text())
            break

        elif vyber == 3:
            print("UKONČUJI")
            exit()

        else:
            print("NESPRÁVNÁ VOLBA, ZVOLTE ZNOVU")
