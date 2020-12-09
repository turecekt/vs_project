"""Prvočísla."""

# Imports
import math
import random
# […]

__author__ = 'Daniel Jurča'
__version__ = '0.1.0'
__email__ = 'd_jurca@utb.cz'
__status__ = 'Work in progress'


def VolbaAkce():
    """
    Volba metody.

    Uživatel zvolí, jestli chce zjistit,
    zda je zadané číslo n prvočíslo,
    nebo vypsat n prvočísel
    """
    print("Akce:")
    print("1 : Ověření, zda je zadané číslo prvočíslem")
    print("2 : Vypsání n prvočísel")
    akce = input("Vyberte možnost (1/2): ")
    print()
    return akce


def OvereniHodnotyAkce():
    """Ověření, zda je volba akce správná."""
    try:
        global typAkce
        typAkce = int(VolbaAkce())
        if typAkce == 1 or typAkce == 2:
            return True
        else:
            return False
    except ValueError:
        return False


while OvereniHodnotyAkce() is False:
    print("Zadejte číslo 1 nebo 2")


def VolbaCisla():
    """Volba čísla n."""
    zadaneCislo = input("Zadejte číslo n: ")
    return zadaneCislo


def OvereniHodnotyCisla():
    """Ověření, zda je zadané číslo integer."""
    try:
        global cislo
        cislo = int(VolbaCisla())
        if cislo > 0:
            return True
        else:
            return False
    except ValueError:
        return False


while OvereniHodnotyCisla() is False:
    print("n musí být celé číslo")


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
    """Fermatovo prvočíslo, hard metoda."""
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


if typAkce == 1:
    UrciPrvocislo(cislo)
elif typAkce == 2:
    print("2")
else:
    print("bs")
