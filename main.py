# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:53:37 2020

@author: Tomas Adamek
"""
import math

class tris():
    def __init__(self,sA = 0, sB = 0, sC = 0, uA = 0, uB = 0, uC = 0):
        self.sA = sA
        self.sB = sB
        self.sC = sC
        self.uA = uA
        self.uB = uB
        self.uC = uC


        if self.sA > 0 and self.sB > 0 and self.sC > 0:
            self.result = self.tris_sss()

    def __str__(self):

        if isinstance(self.result, dict):
            out = ""
            for x, y in self.result.items():
                out += "{} – {}\n".format(x, y)
        else:
            out = str(self.result)
        return out


    def is_tris(self):
        sA = self.sA
        sB = self.sB
        sC = self.sC
        if sA + sB > sC and sA + sC > sB and sB + sC > sA:
            return True
        else:
            return False

    def tris_sss(self):
        if self.is_tris():
            sA = self.sA
            sB = self.sB
            sC = self.sC
            obvod = sA + sB + sC
            s = obvod / 2
            obsah = math.sqrt(s * (s - sA) * (s - sB) * (s - sC))
            cosA = (sB ** 2 + sC ** 2 - sA ** 2) / (2 * sB * sC)
            cosB = (sA ** 2 + sC ** 2 - sB ** 2) / (2 * sA * sC)
            cosC = (sA ** 2 + sB ** 2 - sC ** 2) / (2 * sA * sC)
            uA = round(math.degrees(math.acos(cosA)), 2)
            uB = round(math.degrees(math.acos(cosB)), 2)
            uC = round(math.degrees(math.acos(cosC)), 2)
            obsah = round(obsah, 2)

            return {"obsah" : str(obsah) + "cm\u00B2",
                    "obvod" : str(obvod) + "cm",
                    "úhel \u03B1" : str(uA) + "°",
                    "úhel \u03B2" : str(uB) + "°",
                    "úhel \u03B3" : str(uC) + "°"}

        else:
            return "Nejedná se o trojúhelník. Součet dvou stran musí být větší než stranatřetí."



sss =tris(3, 3, 3)
print(sss)
