"""Urceni prvocisla."""
def vyzadejCislo():
    """Funkce si vyzada cislo od uzivatele."""
    try:
        vstup = int(input("Vlozte cislo: "))
        return vstup
    except ValueError:
        print("Nespravny format cisla.")
        return "Nespravny format cisla."
def jePrvocislo(cislo):
    """Program vyzada vstup od uzivatele a overi zda se jedna o prvocislo."""
    prvocislo = False
    # Vyzadame vstup od uzivatele ve spravnem formatu.
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
        print(f"Cislo {cislo} NENI prvocislo.")
        return False
        return (f"Cislo {cislo} NENI prvocislo.")
    else:
        print(f"Cislo {cislo} JE prvocislo.")
        return True
        return (f"Cislo {cislo} JE prvocislo.")
if __name__ == '__main__':
    jePrvocislo(vyzadejCislo())
    