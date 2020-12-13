#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 6 16:44:53 2020.

@author: ondrej
"""
import math


def sestrojitelnost(a, b, c):
    """Zjistí zda jde tento trojúhelník sestrojit."""
    if (a + b) > c and (b + c) > a and (c + a) > b:
        return True
    else:
        return False


# obvod obsah
def obvod(a, b, c):
    """Vypocita obvod trojuhelniku."""
    return a + b + c


def obsah(a, b, c):
    """Vypočítá obsah trojúhelníku."""
    s = (a + b + c)/2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def pveta(c, b, a):
    """Vypočítá pythagorovu větu a ověří její pravdivost."""
    cd = c*c
    ab2 = (a * a) + (b * b)

    if (cd == ab2):
        return True
    else:
        return False


def prepona(a, b, c):
    """Urci nejdelsi stranu trojuhelniku."""
    if (a > b):
        if (a > c):
            if (pveta(a, b, c)):
                print("Trojuhelnik je pravouhly")
            else:
                print("Trojuhelnik neni pravoúhly")
        else:
            if (pveta(c, a, b)):
                print("Trojuhelnik je pravouhly")
            else:
                print("Trojuhelnik neni pravoúhly")
    else:
        if (b > c):
            if (pveta(b, a, c)):
                print("Trojuhelnik je pravouhly")
            else:
                print("Trojuhelnik neni pravoúhly")
        else:
            if (pveta(c, a, b)):
                print("Trojuhelnik je pravouhly")
            else:
                print("Trojuhelnik neni pravoúhly")

