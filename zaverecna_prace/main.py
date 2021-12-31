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


def vygeneruj_nahodny_vyraz():
"""Generuje náhodny matematicky vyraz"""
operatory = ["+", "-", "/", "*"] # list operátorů
a = random.randint(-10, 10) # náhodné b číslo v intervalu <-10,10>
b = random.randint(-10, 10) # náhodné a číslo v intervalu <-10,10>
operator = operatory[random.randint(0,3)] # výběr náhodného operátoru z listu operátorů
return f"{​​a}​​ {​​operator}​​ {​​b}​​"


def uloz_nahodny_vyraz():
    """Uložení náhodného vyrazu do globální proměnné pro pozdější použití"""
    global NAHODNY_VYRAZ
    NAHODNY_VYRAZ = vygeneruj_nahodny_vyraz()
    return NAHODNY_VYRAZ


def main():
    pass


if __name__ == "__main__":
    main()

