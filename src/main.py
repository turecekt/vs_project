"""Urceni prvocisla."""


def vyzadejCislo():
    """Funkce si vyzada cislo od uzivatele."""
    try:
        vstup = int(input("Vlozte cislo: "))
        return vstup
    except ValueError:
        return "Nesprávný formát čísla."


def jePrvocislo(cislo):
    """Program vyzada vstup od uzivatele a overi zda se jedna o prvocislo."""
    prvocislo = False
    # Vyzadame vstup on uzivatele ve správném formátu.
    while(isinstance(cislo, int) is False):
        cislo = vyzadejCislo()

    # Zkontrolujeme, zda je cislo delitelne jinym cislem bez zbytku.
    if cislo > 1:
        for i in range(2, cislo):
            if cislo % i == 0:
                prvocislo = True
                break

    # Vypiseme vysledek
    if prvocislo:
        return (f"Cislo {cislo} NENÍ provocislo.")
    else:
        return (f"Cislo {cislo} je prvocislo.")


if __name__ == '__main__':
    jePrvocislo(vyzadejCislo())
