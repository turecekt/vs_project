# -*- coding: utf-8 -*-

"""
Tento soubor obsahuje vlastní průběh programu.

Created on Tue Dec  1 17:32:47 2020

@author: jakub
"""

import classes

"""Vlastní program"""

if __name__ == "__main__":
    print("""Vstupem programu  jsou souřadnice
          vrcholů (tří bodů) ve 2D prostoru""")
    print()
    print("""Program poté sdělí informaci o sestrojitelnosti trojúhelníku,
          informaci o délkách stran, obvod,
          obsah a informaci o tom, zda je trojúhelník pravoúhlý""")
    print()
    print("""Zadejte body A, B a C v 2D prostory, a to ve tvaru
          např. Ax mezera Ay, při úmyslu zadat bod B[3, 7], tedy
          zadám na vyzvání k bodu B číslo 3 7.""")
    First = input("Zadejte souřadnice bodu A: ")
    Second = input("Zadejte souřadnice bodu B: ")
    Third = input("Zadejte souřadnice bodu C: ")
    zadanyTrojuhelnik = classes.vstup(First, Second, Third)
    if zadanyTrojuhelnik.jeSestrojitelny() == "NE":
        a = zadanyTrojuhelnik.delkaStrany("a")
        b = zadanyTrojuhelnik.delkaStrany("b")
        c = zadanyTrojuhelnik.delkaStrany("c")
        result = """
        Trojúhelník z vámi zadaných bodů
        není sestrojitelný, další parametry
        nebudou dopočítávány.
        """
        print(result)
        print()
        input()
    else:
        a = zadanyTrojuhelnik.delkaStrany("a")
        b = zadanyTrojuhelnik.delkaStrany("b")
        c = zadanyTrojuhelnik.delkaStrany("c")
        print("Trojúhelník je sestrojitelný, má následující parametry:")
        print("Delka strany a:")
        print(a)
        print("Delka strany b:")
        print(b)
        print("Delka strany c:")
        print(c)
        print("Obvod:")
        print(zadanyTrojuhelnik.obvod())
        print("Obsah:")
        print(zadanyTrojuhelnik.obsah())
        print("Pravoúhlý:")
        print(zadanyTrojuhelnik.jePravouhly())
        input()
