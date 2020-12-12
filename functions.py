"""Funkce."""

# Import knihovny math pro matematické funkce
import math


# Funkce pro výpočet délky strany AB trojúhelníku
def delkaStranyAB(xa, xb, ya, yb):
    """Funkce vrátí velikost délky strany AB."""
    return math.sqrt(((xb-xa)**2)+(yb-ya)**2)


# Funkce pro výpočet délky strany BC trojúhelníku
def delkaStranyBC(xb, xc, yb, yc):
    """Funkce vrátí velikost délky strany BA."""
    return math.sqrt(((xc-xb)**2)+(yc-yb)**2)


# Funkce pro výpočet délky strany AC trojúhelníku
def delkaStranyAC(xa, xc, ya, yc):
    """Funkce vrátí velikost délky strany AC."""
    return math.sqrt(((xc-xa)**2)+(yc-ya)**2)


# Funkce pro výpočet obvodu trojůhelníku
def obvodTroj(xa, xb, xc, ya, yb, yc):
    """Deklarace proměnných a vložení hodnot."""
    stranaAB = math.sqrt(((xb-xa)**2)+(yb-ya)**2)
    stranaBC = math.sqrt(((xc-xb)**2)+(yc-yb)**2)
    stranaAC = math.sqrt(((xc-xa)**2)+(yc-ya)**2)
    """Funkce vráti délku obvodu."""
    return stranaAB + stranaBC + stranaAC


# Funkce pro výpočet obsahu trojůhelníku
def obsahTroj(xa, xb, xc, ya, yb, yc):
    """Deklarace proměnných a vložení hodnot."""
    strAB = math.sqrt(((xb-xa)**2)+(yb-ya)**2)
    strBC = math.sqrt(((xc-xb)**2)+(yc-yb)**2)
    strAC = math.sqrt(((xc-xa)**2)+(yc-ya)**2)
    """Výpočet poloviny obvodu"""
    pulO = (strAB + strBC + strAC) / 2
    """Funkce vrátí velikost obsahu."""
    return math.sqrt(pulO * (pulO - strAB) * (pulO - strBC) * (pulO - strAC))
