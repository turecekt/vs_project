"""Funkce."""

# Import knihovny math pro matematické funkce
import math


# Funkce pro výpočet délky strany AB trojúhelníku
def delkaStranyAB(xa, xb, ya, yb):
    """Funkce vrátí velikost délky strany AB."""
    return math.sqrt(((xb-xa)**2)+(yb-ya)**2)
