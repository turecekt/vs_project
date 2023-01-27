"""
    Importujeme knižnicu random pre generovanie náhodných čísel,
    pretože ju budeme potrebovať pri heuristickej metóde Miller-Rabin Test
"""
import random

"""
    Funkcia 'prvocislo' na overenie či je číslo prvočíslo
    deterministickou metódou.Delenie od 2 do sqrt(n): Táto
    metóda zahŕňa delenie čísla n od 2 až do jeho druhej
    odmocniny. Ak sa nedá deliť žiadnym číslom v tomto rozsahu,
    potom sa považuje za prvočíslo.
"""


def prvocislo(n):
    # Overenie či číslo je menšie alebo rovné 2
    if n <= 2:
        return n == 2
    # Overenie či číslo je párne
    elif n % 2 == 0:
        return False
    # Iterovanie od 3 po odmocninu z čísla + 1
    for i in range(3, int(n ** 0.5) + 1, 2):
        # Ak sa delí bez zvyšku, nie je to prvočíslo
        if n % i == 0:
            return False
    # Ak sa nenašlo žiadne deliteľné číslo, je to prvočíslo
    return True


"""
    Funkcia 'prvocislo_mr' naoverenie či je číslo prvočíslo
    heuristickou metódou. Miller-Rabin test funguje tak,
    že pre zadané číslo n, prvý krok je rozklad n-1 na d*2^r.
    Potom sa vyberie náhodné číslo a, ktoré sa zvolí z
    intervalu od 2 do n-2. Ďalej sa vykoná výpočet a^d mod n.
    Ak sa výsledok rovná 1 alebo n-1, číslo sa považuje za
    možné prvočíslo a test sa opakuje s iným číslom a.
    Ak sa výsledok nerovná ani 1 ani n-1, prechádza sa
    cez cyklus, kde sa výpočet opakuje s výsledkom
    predchádzajúceho výpočtu, kým sa neobjaví výsledok
    n-1 alebo kým sa nevykoná r-1 iterácií. Ak sa v cykle
    nedosiahne výsledok n-1, číslo sa považuje za zložené.
"""


def prvocislo_mr(n, k=5):
    # Ak je číslo párne alebo delitelné 3, vrátime False.
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Inicializujeme premenné 'r' a 'd' pre kroky Miller-Rabin testu.
    r, d = 0, n - 1
    # rozklad n-1 na d*2^r
    while d % 2 == 0:
        r += 1
        d //= 2
    # Pomocou for cyklu vykonáme 'k' iterácií Miller-Rabin testu
    # s náhodnými číslami od 2 do n-2.
    for _ in range(k):
        a = random.randint(2, n - 2)
        # výpočet a^d mod n
        x = pow(a, d, n)
        """
            Ak sa výsledok nerovná ani 1 ani n-1, prechádza sa cez cyklus,
            kde sa výpočet opakuje s výsledkom predchádzajúceho výpočtu.
            kým sa neobjaví výsledok n-1 alebo kým sa nevykoná r-1 iterácií.
        """
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            """
                Ak sa v cykle nedosiahne výsledok n-1,
                číslo sa považuje za zložené.
            """
            if x == n - 1:
                break
        else:
            return False
    return True


while True:
    """
        Vstup čísla od používateľa a jeho ošetrienie aby bolo
        číslo zadané užívateľom kladné celé číslo.
    """
    try:
        cislo = int(input("Zadaj cislo: "))
        # Podmienka na overenie kladnosti čísla.
        if cislo <= 0:
            print("Zadaj kladne celo cislo.")
            continue
        break
    # Výpis chybovej hlášky ak sa zadal vstup iný ako typ int
    except ValueError:
        print("Zadaj validne cele cislo.")

# Volanie funkcií
"""
    Ak je číslo väčšie ako 1000 zavolá funkciu 'prvocislo_mr', čiže
    heuristickú metódu Miller-Rabin test.
"""
if cislo > 1000:
    if prvocislo_mr(cislo):
        print(f"{cislo} je prvocislo."
              f" Pouzita heuristicka metoda: Miller-Rabin test.")
    else:
        print(f"{cislo} nie je prvocislo. "
              f"Pouzita heuristicka metoda: Miller-Rabin test.")
    """
        Ak je číslo menšie alebo rovno 1000 zavolá funkciu 'prvocislo',
        čiže metódu delenia od 2 do sqrt(n)
    """
else:
    if prvocislo(cislo):
        print(f"{cislo} je prvocislo. Pouzita deterministicka metoda.")
    else:
        print(f"{cislo} nie je prvocislo. Pouzita deterministicka metoda.")
