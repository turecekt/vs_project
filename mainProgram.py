"""Hlavní program."""

# Import souboru functions.py
import functions

# Zadání vstupních hodnot uživatelem a uložení je do přoměnných
xA = input("Zadej x-ovou souřadnici bodu A: ")
yA = input("Zadej y-ovou souřadnici bodu A: ")
xB = input("Zadej x-ovou souřadnici bodu B: ")
yB = input("Zadej y-ovou souřadnici bodu B: ")
xC = input("Zadej x-ovou souřadnici bodu C: ")
yC = input("Zadej y-ovou souřadnici bodu C: ")

# Podmínka pro zkontrolování vstupních hodnot
if functions.souradniceJeCislo(xA, xB, xC, yA, yB, yC) == 1:
    "Předělání vstupních hodnot na čísla typu float"
    xA = float(xA.replace(',', '.'))
    yA = float(yA.replace(',', '.'))
    xB = float(xB.replace(',', '.'))
    yB = float(yB.replace(',', '.'))
    xC = float(xC.replace(',', '.'))
    yC = float(yC.replace(',', '.'))
