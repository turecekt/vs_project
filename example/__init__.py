"""Výpočet vlastností trojuhelníka."""
import math


def ask(prompt, default):
    """Funkce pro zachycení souřadnic zadaných uživatele."""
    vstup = input(prompt)
    try:
        val = int(vstup)
    except ValueError:
        print("Špatně zadaná hodnota.")
        print("Použije se defaultní hodnota - ", default)
        val = default
    return val


def is_valid(Triangle):
    """Funkce is_valid vyhodnotí je-li daný trojuhelník sestrojitelný."""
    return True


def side_lengths(Triangle):
    """Funkce side_lengths vrací list délek stran trojuhelníku."""
    A = Triangle[0]
    B = Triangle[1]
    C = Triangle[2]
    a = abs(math.sqrt((B[0] - C[0])**2+(B[1] - C[1])**2))
    b = abs(math.sqrt((C[0] - A[0])**2+(C[1] - A[1])**2))
    c = abs(math.sqrt((A[0] - B[0])**2+(A[1] - B[1])**2))
    sides = [a, b, c]
    return sides


def circumference(Triangle):
    """Funkce circumference vrací obvod trojuhelníku."""
    obvod = 5
    return obvod


def is_right(Triangle):
    """Funkce is_right vyhodnotí je-li daný trojuhelník pravoúhlý."""
    return False


"""Zaznamenat vstup z konzole"""
print("Zadejte souřadnice trojuhelníku\n")
A = (ask("bod A - souřadnice x: ", 0), ask("bod A - souřadnice y: ", 0))
B = (ask("bod B - souřadnice x: ", 3), ask("bod B - souřadnice y: ", 0))
C = (ask("bod C - souřadnice x: ", 0), ask("bod C - souřadnice y: ", 4))
Triangle = [A, B, C]
print("\nZadali jste Trojuhelník se souřadnicemi:")
print("A: ", A)
print("B: ", B)
print("C: ", C)
