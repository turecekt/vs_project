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
