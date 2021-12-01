#!/usr/bin/python3
"""Program pro převod celého čísla mezi číselnými soustavami."""

import sys
import os

# Zobrazí chybovou hlášku se barevným a zvýrazněním na VT100 terminálech
_TERMINAL_NUMBER_ERROR = """\
Zadejte\033[33;1m celé\033[22;0m číslo v\
\033[33;1m desítkové\033[22;0m soustavě!\
"""

# Zobrazí chybovou hlášku i na té hrůze cmd.exe
_CMD_NUMBER_ERROR = "Zadejte celé číslo v desítkové soustavě"

# ========= Zadání =========
# VSTUP
# Kladné celé číslo v desítkové soustavě
# Cílová soustava (2, 8, 16, apod.)
# Bude čistě na řešitelském týmu, aby vymyslelo vhodný způsob zadávání vstupu
# (parametricky, dotazy na uživatele, či jinak).
# VÝSTUP
#
# Číslo v cílové číselné soustavě

HEX_TABULKA = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
               6: "6", 7: "7", 8: "8", 9: "9", 10: "A",
               11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def toHex(num):
    """Převede číslo na zobrazení v hexadecimální soustavě."""
    # Ověříme že jsme opravdu dostaly číslo
    try:
        num = int(num)
    except ValueError:  # Jinak si ho necháme znova vybrat
        num = getInput()

    zbytek = num
    ret = ""  # Výsledek
    while num > 0:
        zbytek = num % 16
        # // dělá int dělení což je přesně naruby od všech ostatních jazyků
        num = num // 16
        ret += HEX_TABULKA[zbytek]

    return "0x" + ret[::-1]  # Vrátí string převrácený


def toBin(num):
    """Převede číslo na zobrazení v binární soustavě."""
    # Ověříme že jsme opravdu dostaly číslo
    try:
        num = int(num)
    except ValueError:  # Jinak si ho necháme znova vybrat
        num = getInput()

    zbytek = num
    ret = ""

    while num > 0:
        zbytek = num % 2
        num = num // 2
        ret += str(zbytek)

    return "0b" + ret[::-1]


def toOctal(num):
    """Převede číslo na zobrazení v octální soustavě."""
    # Ověříme že jsme opravdu dostaly číslo
    try:
        num = int(num)
    except ValueError:  # Jinak si ho necháme znova vybrat
        num = getInput()

    zbytek = num
    ret = ""

    while num > 0:
        zbytek = num % 8
        num = num // 8
        ret += str(zbytek)

    return "0o" + ret[::-1]


def getInput():
    """Donutí uživatele zadat celé číslo které následně vrátí."""
    while (True):
        try:
            return int(input("Zadejte celé číslo: "))
        except ValueError:
            if not os.name == "posix":
                print(_CMD_NUMBER_ERROR)
            else:
                print(_TERMINAL_NUMBER_ERROR)
        except EOFError:  # Uživatel poslal jen EOF (^D)
            print()       # Před ukončením pošleme \n aby se mu odsadila shell
            sys.exit(0)


def main(args=None):
    """Vstupní funkce."""
    cisloKprevodu = 0
    # Použití bude -b [číslo] -hex hexadecimal -o octal
    # Pokud nezadá číslo tak se na něj zeptáme, pokud nezadá výstupní typ
    # tak vypíšeme všechny

    # Nic jsme nedostaly, převádíme na vše, číslo získáme interaktivně
    if len(args) == 0:
        cisloKprevodu = getInput()
        print(toHex(cisloKprevodu))
        print(toBin(cisloKprevodu))
        print(toOctal(cisloKprevodu))
        # Čistě interaktivní funkce takže návratová hodnota není potřeba
        return None
    elif len(args) > 2 or args[0] == "--help":  # Máme buď typ nebo číslo
        print("Použití:")
        print("python3 soustavy.py -[cílová soustava] [číslo k převodu]")
        print("Možné soustavy:\n\t-b binární\n\t-h šestnáctková")
        print("\t-o osmičková")
        print("Pokud spuštěno bez argumentů, číslo bude zjištěno interaktivně")
        print("a výstupem budou všechny soustavy")
        sys.exit(1)
    else:  # Hlavní parsování
        # Na číslo převádíme automaticky v každé metodě takže zde
        # kontrola být nemusí
        vysledek = 0
        if args[0] == "-h":
            vysledek = toHex(args[1])
        elif args[0] == "-b":
            vysledek = toBin(args[1])
        elif args[0] == "-o":
            vysledek = toOctal(args[1])
        else:
            print("Neznámý přepínač: " + args[0])
            print("Zkuste --help pro nápovědu")
            sys.exit(1)
    print(vysledek)
    return vysledek  # Ještě vracíme kvůli testům


if __name__ == "__main__":
    main(sys.argv[1:])
