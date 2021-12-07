"""Funkce které později budou přesunuty do souboru __init__.py."""
import example
import math


def sestrojitelnost(Triangle):
    """Funkce vypíše jeli trojuhelnik sestrojitelný."""
    sides = example.side_lengths(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        print("Trojuhelnik je sestrojitelny")
    else:
        print("Trojuhelnik neni sestrojitelny")


def informace(Triangle):
    """Funkce vypíše nejdelší a nejkratší stranu."""
    sides = example.side_lengths(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))
    max = a
    min = a
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
    # Vypis max
    if (max == a):
        print("Nejdelsi strana: a = "+str(max))
    if (max == b):
        print("Nejdelsi strana: b = "+str(max))
    if (max == c):
        print("Nejdelsi strana: c = "+str(max))
    # Vypis min
    if (min == a):
        print("Nejkratsi strana: a = "+str(min))
    if (min == b):
        print("Nejkratsi strana: b = "+str(min))
    if (min == c):
        print("Nejkratsi strana: c = "+str(min))


def obvod_obsah(Triangle):
    """Funkce vypíše obvod a obsah."""
    sides = example.side_lengths(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    Obvod = a + b + c
    s = Obvod / 2
    S = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Obvod: "+str(Obvod)+"\n"+"Obsah: "+str(S))


def pravouhlost(Triangle):
    """Funkce vypíše jeli trojuhelnik pravoúhlý."""
    sides = example.side_lengths(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (c == math.sqrt(a**2 + b**2)):
        print("Trojuhelnik je pravouhly")
    else:
        print("Trojuhelnik neni pravouhly")
