# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:53:37 2020

@author: User
"""
import math

def troj_sss(sA, sB, sC):
    obvod = sA + sB + sC
    cosA = (sB ** 2 + sC ** 2 - sA ** 2) / (2 * sB * sC)
    cosB = (sA ** 2 + sC ** 2 - sB ** 2) / (2 * sA * sC)
    cosC = (sA ** 2 + sB ** 2 - sC ** 2) / (2 * sA * sC)
    uA = round(math.degrees(math.acos(cosA)), 2)
    uB = round(math.degrees(math.acos(cosB)), 2)
    uC = round(math.degrees(math.acos(cosC)), 2)
    s = obvod / 2
    obsah = math.sqrt(s * (s - sA) * (s - sB) * (s - sC))
    trojuhelnik = {"obsah" : str(obsah) + "cm\u00B2",
                   "obvod" : str(obvod) + "cm",
                   "úhel \u03B1" : str(uA) + "°",
                   "úhel \u03B2" : str(uB) + "°",
                   "úhel \u03B3" : str(uC) + "°"}
    return trojuhelnik

sss = troj_sss(3, 4, 5)
for x, y in sss.items():
    print("{} – {}".format(x, y))