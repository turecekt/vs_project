from projekt_pucek_2021 import PrevodR


def test_prevodnarim():
    """Testovací příkazy."""
    assert PrevodR.narim(3999) == 'MMMCMXCIX'
    assert PrevodR.narim(3888) == 'MMMDCCCLXXXVIII'
    assert PrevodR.narim(2421) == 'MMCDXXI'
    assert PrevodR.narim(15) == 'XV'


def test_prevodnaar():
    assert PrevodR.naar("MMMCMXCIX") == 3999
    assert PrevodR.naar("MMMDCCCLXXXVIII") == 3888
    assert PrevodR.naar("MMCDXXI") == 2421
    assert PrevodR.naar("XV") == 15


if __name__ == "__main__":
    # Deklarace proměnné typu string,
    # která následně určuje, jestli se má program ukončit
    zadani = " "

    # Cyklus, při kterém program běží, dokud
    # není na konci zadáno A pro ukončení
    while zadani.lower() != 'a':
        rimZad = " "
        arZad = 0

        # Cyklus, při kterém běží input do doby,
        # než uživatel zadá validní hodnotu
        while PrevodR.naar(rimZad) < 1 or PrevodR.naar(rimZad) > 3999:
            rimZad = input("Zadej římské: ")

            # Obsahuje-li římské zadání číslo, jedná se o chybu
            if rimZad.isnumeric():
                print("Nezadal jsi římské číslo.")

            # Pokud je vše zadáno správně, program pokračuje dál
            else:
                # Pokud se výsledek nachází v intervalu
                # pro platnost, program vypíše výsledek
                if 0 < PrevodR.naar(rimZad.upper()) < 4000:
                    print(rimZad.upper() + str(" = ") + str(PrevodR.naar(rimZad.upper())))

                # Je-li výsledná hodnota mimo interval
                # pro platnost, program zahlásí chybu
                else:
                    print("Chybné zadání.")

        # Cyklus, který běží po dobu, dokud není správně zadané číslo
        while arZad < 1 or arZad > 3999:
            arZad = str(input("Zadej arabské: "))

            # Kontrola, jestli bylo správně zadáno číslo v zadání
            if arZad.isnumeric():
                arZad = int(arZad)
                # Převod proměnné typu string na integer

                # Pokud se zadané číslo nenachází v
                # platném rozsahu, program zahlásí chybu
                if arZad < 1 or arZad > 3999:
                    print("Chybné zadání.")

                # V opačném případě se provede převod
                else:
                    print(str(arZad) + str(" = ") + PrevodR.narim(arZad))

            # Nebylo-li zadáno číslo, program zahlásí chybu
            else:
                print("Nezadal jsi číslo.")
                arZad = 0
                # Zápis hodnoty, aby při špatném zadání neskončil cyklus

        # Ukončovací dialog programu
        zadani = input("Přejete si ukončit program? (A/N)\n")
