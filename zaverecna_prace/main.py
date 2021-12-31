# ------------------------------------------------------------
# REAKCNI RYCHLOSTI
# Program se postupně dotazuje uživatele na výsledek pěti pseudonáhodně generovaných
# jednoduchých výrazů a [+-*/] b ( a , b∈⟨−10,10⟩ ), přičemž měří reakční dobu a
# vyhodnocuje správnost.
# VSTUP
# • Reakce uživatele na příklady v podobě zadaných výsledků
# VÝSTUP
# • Informace o úspěšnosti (kolikrát bylo zodpovězeno správně),
# • Informace o průměrné reakční době.
# Autoři: Filip Chromý, Drahomíra Šťastná, Jan Fojtík, Tomáš Blabla
# ------------------------------------------------------------

import random
import time

RYCHLOSTI_REAKCI = [] # Globální list pro uložení reakčních rychlostí
POCET_SPRAVNYCH_ODPOVEDI = 0
NAHODNY_VYRAZ = ""


def vygeneruj_nahodny_vyraz():
    """Generuje náhodny matematicky vyraz"""
    operatory = ["+", "-", "/", "*"] # list operátorů
    a = random.randint(-10, 10) # náhodné b číslo v intervalu <-10,10>
    b = random.randint(-10, 10) # náhodné a číslo v intervalu <-10,10>
    operator = operatory[random.randint(0,3)] # výběr náhodného operátoru z listu operátorů
    return f"{a} {operator} {b}"


def uloz_nahodny_vyraz():
    """Uložení náhodného vyrazu do globální proměnné pro pozdější použití"""
    global NAHODNY_VYRAZ
    NAHODNY_VYRAZ = vygeneruj_nahodny_vyraz()
    return NAHODNY_VYRAZ


def vstup_uzivatele():
    """Přečte a zkontroluje platnost vstupu uživatele"""
    vysledek = input(f"Vypocitej: {NAHODNY_VYRAZ} = ")
    try:
        vysledek = float(vysledek)
        return vysledek
    except:
        print("Zadan neplatny vstup")


def odecti(a, b):
    """odecte hodnotu parametru b od a"""
    try:
    return a - b
    except:
    raise ValueError


def vynasob(a, b):
    """Vynásobí hodnoty parametrů a a b"""
    try:
    return int(a * b)
    except:
    raise ValueError


def vydel(a, b):
    """Vydělí hodnotu parametru a hodnotou b"""
    if b == 0:
    return 0
    lse:
    try:
    return a / b
    except:
    raise ValueError


def secti(a, b):
    """sečte hodnoty parametrů a a b"""
    try:
    return a + b
    except:
    raise ValueError


def main():
    pass


if __name__ == "__main__":
    main()

