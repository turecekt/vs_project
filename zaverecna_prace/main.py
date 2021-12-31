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
    else:
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


def vyhodnot_vstup_uzivatel():
    """Vyhodnotí vysledek nahodneho vyrazu a porovná jej se vstupem uživatele"""
    global NAHODNY_VYRAZ
    a = NAHODNY_VYRAZ.split(" ")[0] # přístup k elementu a ve výrazu
    oper = NAHODNY_VYRAZ.split(" ")[1] # přístup k operátoru ve výrazu
    b = NAHODNY_VYRAZ.split(" ")[2] # přístup k elementu b ve výrazu
    if oper == "+":
        vysledek = secti(int(a), int(b))
    elif oper == "-":
        vysledek = odecti(int(a), int(b))
    elif oper == "/":
        vysledek = vydel(int(a), int(b))
    elif oper == "*":
        vysledek = vynasob(int(a), int(b))
    vysledek_uzivatele = vstup_uzivatele()
    if vysledek_uzivatele == float(vysledek): # kontrola správnosti výsledků zadaného uživatelem
        global POCET_SPRAVNYCH_ODPOVEDI
        POCET_SPRAVNYCH_ODPOVEDI = POCET_SPRAVNYCH_ODPOVEDI + 1 # inkrementace počtu správných odpovědí


def prumerna_reakcni_rychlost():
    """Vypočte průměrnou reakčni rychlost"""
    return sum(RYCHLOSTI_REAKCI) / len(RYCHLOSTI_REAKCI)


def vytvor_test():
    """Vytvoří test o 5 příkladech a vyhodnotí počet správných odpovědí a průměrnou reakční rychlost"""
    global RYCHLOSTI_REAKCI
    print("Vypocti nasledujících 5 výrazů")
    input("Pro start stiskni ENTER: ")
    print("\n")
    for i in range(5):
        start = time.time()
        uloz_nahodny_vyraz()
        vyhodnot_vstup_uzivatel()
        end = time.time()
        RYCHLOSTI_REAKCI.append(end - start)

    print(f"\nPocet spravnych odpovedi: {POCET_SPRAVNYCH_ODPOVEDI} z 5") # Vytisteni poctu spravnych odpovedi    
    print(f"Prumerna reakcni rychlost: %.2fs" %prumerna_reakcni_rychlost(RYCHLOSTI_REAKCI)) # Vytisteni prumerneho reakcni rychlosti
    input("\nPro ukončení stiskněte ENTER")


def main():
    vytvor_test()


if __name__ == "__main__":
    main()

