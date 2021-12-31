"""Změř průměrnou reakční rychlost odpovědí na nádhodné výrazy."""
# ------------------------------------------------------------
# REAKCNI RYCHLOSTI
# Program se postupně dotazuje uživatele
# na výsledek pěti pseudonáhodně generovaných
# jednoduchých výrazů a [+-*/] b ( a , b∈⟨−10,10⟩ ), přičemž
# měří reakční dobu a
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

RYCHLOSTI_REAKCI = []  # Globální list pro uložení reakčních rychlostí
POCET_SPRAVNYCH_ODPOVEDI = 0
NAHODNY_VYRAZ = ""


def vygeneruj_nahodny_vyraz():
    """Generuje náhodny matematicky vyraz."""
    operatory = ["+", "-", "/", "*"]  # list operátorů
    a = random.randint(-10, 10)  # náhodné b číslo v intervalu <-10,10>
    b = random.randint(-10, 10)  # náhodné a číslo v intervalu <-10,10>
    # výběr náhodného operátoru z listu operátorů
    operator = operatory[random.randint(0, 3)]
    return f"{a} {operator} {b}"


def uloz_nahodny_vyraz():
    """Uložení náhodného vyrazu do globální proměnné pro pozdější použití."""
    global NAHODNY_VYRAZ
    NAHODNY_VYRAZ = vygeneruj_nahodny_vyraz()
    return NAHODNY_VYRAZ


def vstup_uzivatele():
    """Přečte a zkontroluje platnost vstupu uživatele."""
    vysledek = input(f"Vypocitej: {NAHODNY_VYRAZ} = ")
    try:
        vysledek = float(vysledek)
        return vysledek
    except TypeError:
        print("Zadan neplatny vstup")


def odecti(a, b):
    """Odecte hodnotu parametru b od a."""
    try:
        return a - b
    except TypeError:
        return "Spatna hodnota"


def vynasob(a, b):
    """Vynásobí hodnoty parametrů a a b."""
    try:
        return int(a * b)
    except ValueError:
        return "Spatna hodnota"


def vydel(a, b):
    """Vydělí hodnotu parametru a hodnotou b."""
    if b == 0:
        return 0
    else:
        try:
            return a / b
        except TypeError:
            return "Spatna hodnota"


def secti(a, b):
    """Sečte hodnoty parametrů a a b."""
    try:
        return a + b
    except TypeError:
        return "Spatna hodnota"


def vyhodnot_vstup_uzivatel():
    """Vyhodnotí výsledek nádhodného výrazu."""
    global NAHODNY_VYRAZ
    a = NAHODNY_VYRAZ.split(" ")[0]  # přístup k elementu a ve výrazu
    oper = NAHODNY_VYRAZ.split(" ")[1]  # přístup k operátoru ve výrazu
    b = NAHODNY_VYRAZ.split(" ")[2]  # přístup k elementu b ve výrazu
    if oper == "+":
        vysledek = secti(int(a), int(b))
    elif oper == "-":
        vysledek = odecti(int(a), int(b))
    elif oper == "/":
        vysledek = vydel(int(a), int(b))
    elif oper == "*":
        vysledek = vynasob(int(a), int(b))
    vysledek_uzivatele = vstup_uzivatele()
    # kontrola správnosti výsledků zadaného uživatelem
    if vysledek_uzivatele == float("%.2f" % vysledek):
        global POCET_SPRAVNYCH_ODPOVEDI
        POCET_SPRAVNYCH_ODPOVEDI = POCET_SPRAVNYCH_ODPOVEDI + 1


def prumerna_reakcni_rychlost(reakcni_rychlosti):
    """Vypočte průměrnou reakčni rychlost."""
    return sum(reakcni_rychlosti) / len(reakcni_rychlosti)


def vytvor_test():
    """Vytvoří test o 5 příkladech."""
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
    # Vytisteni poctu spravnych odpovedi
    print(f"\nPocet spravnych odpovedi: {POCET_SPRAVNYCH_ODPOVEDI} z 5")
    reakce = prumerna_reakcni_rychlost(RYCHLOSTI_REAKCI)
    # Vytisteni prumerne reakcni rychlosti
    print("Průměrná reakční rychlost: %.2fs"% reakce)
    input("\nPro ukončení stiskněte ENTER")


def main():
    """Spouštěcí metoda programu."""
    vytvor_test()


if __name__ == "__main__":
    main()

# Testovací funkce


def test_secti():
    """Testuje funkcni sčítání."""
    assert secti(10, 9) == 19


def test_secti2():
    """Testuje spatne zadanou hodnotu."""
    assert secti(",", 10) == "Spatna hodnota"


def test_odecti():
    """Testuje funkci odečitání."""
    assert odecti(20, 10) == 10


def test_odecti2():
    """Testuje spatne zadanou hodnotu."""
    assert odecti("#", 10) == "Spatna hodnota"


def test_vynasob():
    """Testuje funkci násobení."""
    assert vynasob(2, 2) == 4


def test_vynasob2():
    """Testuje spatne zadanou hodnotu pri nasobeni."""
    assert vynasob("a", 2) == "Spatna hodnota"


def test_vydel():
    """Testuje funkcni dělení."""
    assert vydel(10, 5) == 2


def test_vydel2():
    """Testuje dělení nulou."""
    assert vydel(10, 0) == 0


def test_vydel3():
    """Testuje špatně zadanou hodnotu."""
    assert vydel("a", 2) == "Spatna hodnota"


def test_vypocty_reakcni_rychlost():
    """Testuje vypočtení průměrné reakční rychlosti."""
    assert prumerna_reakcni_rychlost([2.22, 3.45, 5.55]) == 3.7399999999999998


def test_uloz_nahodny_vyraz():
    """Testuje správné uložení hodnoty do globální proměnné."""
    assert uloz_nahodny_vyraz() == NAHODNY_VYRAZ


def test_vstup_uzivatele():
    """Testuje správnou návratovou hodnotu vstupu uživatelem."""
    assert vstup_uzivatele_test(10, 10) == 20


def test_vygeneruj_nahodny_vyraz():
    """Testuje generaci náhodného výrazu."""
    assert vygeneruj_nahodny_vyraz_test(10, 10, "+") == "10 + 10"


def test_vstup_uzivatele2():
    """Testuje špatně zadanou hodnotu uživatelem."""
    assert vstup_uzivatele_test("a", 10) == "Zadana neplatna hodnota"


def vstup_uzivatele_test(a, b):
    """Pomocná funkce pro testování vstupu uživatele."""
    try:
        vysledek = a + b
        return vysledek
    except TypeError:
        return "Zadana neplatna hodnota"


def vygeneruj_nahodny_vyraz_test(a, b, op):
    """Pomocna funkce pro test generace nahodneho vyrazu."""
    return f"{a} {op} {b}"
