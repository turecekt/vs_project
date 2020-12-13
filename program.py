# -*- coding: utf-8 -*-

"""
Tento soubor obsahuje vlastní průběh programu.

Created on Tue Dec  1 17:32:47 2020

@author: jakub
"""

import classes

"""Vlastní program"""

zadanyTrojuhelnik = classes.vstup()
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
