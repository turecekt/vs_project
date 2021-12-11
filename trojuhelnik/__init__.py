"""Výpočet vlastností trojuhelníka."""
import math
import sys


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


def sestrojitelnost(Triangle):
    """Funkce vypíše jeli trojuhelnik sestrojitelný."""
    A = Triangle[0]
    B = Triangle[1]
    C = Triangle[2]

    x = (A[0]*(B[1] - C[1])+B[0]*(C[1] - A[1])+C[0]*(A[1] - B[1]))

    if x == 0:
        return False
    else:
        return True


def delky_stran(Triangle):
    """Funkce delky_stran vrací list délek stran trojuhelníku."""
    A = Triangle[0]
    B = Triangle[1]
    C = Triangle[2]
    a = abs(math.sqrt((B[0] - C[0])**2+(B[1] - C[1])**2))
    b = abs(math.sqrt((C[0] - A[0])**2+(C[1] - A[1])**2))
    c = abs(math.sqrt((A[0] - B[0])**2+(A[1] - B[1])**2))
    sides = [a, b, c]
    return sides


def serad_strany(Triangle):
    """Funkce vypíše nejdelší a nejkratší stranu."""
    sides = delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]

    max = a
    min = a
    mid = a
    # Nejdelsi strana
    if b > max:
        max = b
    if c > max:
        max = c
    # Nejkratsi strana
    if b < min:
        min = b
    if c < min:
        min = c
    # Mid
    if ((b != max) and (b != min)):
        mid = b
    if ((c != max) and (c != min)):
        mid = c
    sides = [max, mid, min]
    return sides


def obvod(Triangle):
    """Funkce obvod vrací obvod trojuhelníku."""
    sides = delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    obvod = a + b + c
    return obvod


def obsah(Triangle):
    """Funkce obsah vrací obsah trojuhelníku."""
    sides = delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    Obvod = a + b + c
    s = Obvod / 2
    S = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return S


def pravouhlost(Triangle):
    """Funkce pravouhlost vyhodnotí je-li daný trojuhelník pravoúhlý."""
    sides = serad_strany(Triangle)
    c = sides[0]
    b = sides[1]
    a = sides[2]
    if (c == math.sqrt(a**2 + b**2)):
        return True
    else:
        return False


"""Zaznamenat vstup z konzole"""
print("Zadejte souřadnice trojuhelníku\n")
A = (0, 0)
B = (3, 0)
C = (0, 4)


if len(sys.argv) > 1:   # Zadal-li uživatel právě jeden argument = "-i"
    print(sys.argv[1])  # pak se přepne do interaktivního módu
    if sys.argv[1] == "-i":
        A = (ask("bod A - souřadnice x:", 0), ask("bod A - souřadnice y:", 0))
        B = (ask("bod B - souřadnice x:", 3), ask("bod B - souřadnice y:", 0))
        C = (ask("bod C - souřadnice x:", 0), ask("bod C - souřadnice y:", 4))

Triangle = [A, B, C]
print("\nZadali jste trojuhelník se souřadnicemi:")
print("A: ", A)
print("B: ", B)
print("C: ", C)

if not sestrojitelnost(Triangle):
    print("\nTrojuhelnik neni sestrojitelny\n")
else:
    print("\nTrojuhelnik je sestrojitelny\n")

    sides = delky_stran(Triangle)
    print("strana a: " + str(sides[0]))
    print("strana b: " + str(sides[1]))
    print("strana c: " + str(sides[2]))

    sides = serad_strany(Triangle)
    print("\nnejdelší strana: " + str(sides[0]))
    print("prostřední strana: " + str(sides[1]))
    print("nejkratší strana: " + str(sides[2]))

    print("\nObvod: "+str(obvod(Triangle)))
    print("\nObsah: "+str(obsah(Triangle)))

    if pravouhlost(Triangle):
        print("\nTrojuhelnik je pravouhly")
    else:
        a = sides[0]
        b = sides[1]
        c = sides[2]
        if (a == b == c):
            print("\nTrojuhelník je rovnostranný")
        else:
            if (((a == b != c)) or ((a == c != b)) or ((b == c != a))):
                print("\nTrojuhelník je rovnoramenný")
