"""Prvočísla."""

# Imports
import math
import random

__author__ = 'Daniel Jurča'
__version__ = '0.4.0'
__email__ = 'd_jurca@utb.cz'
__status__ = 'Work in progress'


def VolbaAkce():
    """
    Volba metody.

    Uživatel zvolí, jestli chce zjistit,
    zda je zadané číslo n prvočíslo,
    nebo vypsat prvočísla po číslo n
    >>>VolbaAkce()
    Akce:
    1 : Ověření, zda je zadané číslo prvočíslem
    2 : Vypsání prvočísel po n
    """
    print("Akce:")
    print("1 : Ověření, zda je zadané číslo prvočíslem")
    print("2 : Vypsání prvočísel po n")
    global akce
    akce = input("Vyberte možnost (1/2): ")
    print()
    return akce


def OvereniHodnotyAkce(akce):
    """Ověření, zda je volba akce správná."""
    try:
        global typAkce
        typAkce = int(akce)
        if typAkce == 1 or typAkce == 2:
            return True
        else:
            return False
    except ValueError:
        return False


def VolbaCisla():
    """Volba čísla n."""
    global zadaneCislo
    zadaneCislo = input("Zadejte číslo n: ")
    return zadaneCislo


def OvereniHodnotyCisla(zadaneCislo):
    """Ověření, zda je zadané číslo integer."""
    try:
        global cislo
        cislo = int(zadaneCislo)
        if cislo > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def Determinacni(cislo):
    """Jednoduchá metoda."""
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(cislo):
        if cislo % i == 0:
            return False
        i = i+2

    return True


def Fermat(cislo):
    """Fermatovo prvočíslo, složitější metoda."""
    if (cislo > 1):
        for time in range(3):
            nahodneCislo = random.randint(2, cislo)-1
            if (pow(nahodneCislo, cislo-1, cislo) != 1):
                return False
        return True
    else:
        return False


def UrciPrvocislo(cislo):
    """Určení prvočísla."""
    if cislo < 1000:
        if Determinacni(cislo) is True:
            print("Je prvočíslo")
        else:
            print("Není prvočíslo")
        print("Metoda: determinační")
    elif cislo >= 1000:
        if Fermat(cislo) is True:
            print("Je prvočíslo")
        else:
            print("Není prvočíslo")
        print("Metoda: Statistická - Fermatova")


def VypisPrvocisel(cislo):
    """Výpis prvočísel do čísla n."""
    print("Prvočísla: ")
    for num in range(2, cislo):
        if all(num % i != 0 for i in range(2, num)):
            print(num, end=" ")


def ProvedAkci(typAkce):
    """Provede zvolenou akci."""
    if typAkce == 1:
        UrciPrvocislo(cislo)
    elif typAkce == 2:
        VypisPrvocisel(cislo)
    else:
        print("Chyba u volby akce")


def main():
    """Spuštění programu."""
    VolbaAkce()
    while OvereniHodnotyAkce(akce) is False:
        print("Zadejte číslo 1 nebo 2")
        print()
        VolbaAkce()
    VolbaCisla()
    while OvereniHodnotyCisla(zadaneCislo) is False:
        print("n musí být celé číslo")
        print()
        VolbaCisla()
    ProvedAkci(typAkce)


if __name__ == "__main__":
    main()
