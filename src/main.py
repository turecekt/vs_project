"""Urceni prvocisla."""
def vyzadejCislo():
    """Funkce si vyzada cislo od uzivatele."""
    try:
        vstup = int(input("Vlozte cislo: "))
        return vstup
    except ValueError:
        print("Nesprávný formát čísla.")
        return "Nesprávný formát čísla."



def jePrvocislo(cislo):
    """Program vyzada vstup od uzivatele a overi zda se jedna o prvocislo."""
    prvocislo = False
    # Vyzadame vstup od uzivatele ve správném formátu.
    while(isinstance(cislo, int) is False):
        cislo = vyzadejCislo()
    # Zkontrolujeme, zda je cislo delitelne jinym cislem bez zbytku.
    if cislo > 1:
        for i in range(2, cislo):
            if cislo % i == 0:
                prvocislo = True         
                break
    else:            
        prvocislo = True

    # Vypiseme vysledek
    if prvocislo:
        print(f"Cislo {cislo} NENÍ provocislo.")
        return False
        return (f"Cislo {cislo} NENÍ provocislo.")
    else:
        print(f"Cislo {cislo} je prvocislo.")
        return True
        return (f"Cislo {cislo} je prvocislo.")


if __name__ == '__main__':
    jePrvocislo(vyzadejCislo())