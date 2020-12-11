# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:53:37 2020.

@author: Tomas Adamek
"""
import math


class Tris():
    """
    Funkce pro vypocet vsech hodnot trojuhelniku.

    Je nutne vlozit 3 hodnoty.
    strana a = sA
    strana b = sB
    strana c = sC
    uhel \u03B1 = uA
    uhel \u03B2 = uB
    uhel \u03B3 = uC
    """

    def __init__(self, sA=0, sB=0, sC=0, uA=0, uB=0, uC=0):
        """
        Konsruktor.

        Vytvori promene pro metody a rozhodne jakou metodu vyuzit
        pro vypocitani dalsich promenych
        """
        self.sA = sA
        self.sB = sB
        self.sC = sC
        self.uA = uA
        self.uB = uB
        self.uC = uC

        if self.sA > 0 and self.sB > 0 and self.sC > 0:
            self.result = self.tris_sss()

    def __str__(self):
        """Pripravuje data pro funkci print.

        Slovníky upravý do pěkného tvaru,
        text vrátí
        """
        if isinstance(self.result, dict):
            out = ""
            for x, y in self.result.items():
                out += "{} – {}\n".format(x, y)
        else:
            out = str(self.result)
        return out

    def is_tris(self):
        """Zjisti jestli je mozne trojuhelnik slozit.

        vraci True nebo False
        """
        sA = self.sA
        sB = self.sB
        sC = self.sC
        if sA + sB > sC and sA + sC > sB and sB + sC > sA:
            return True
        else:
            return False

    def tris_sss(self):
        """Metoda pro vypocet podle vety sss.

        Vraci slovnik ci string
        """
        if self.is_tris():
            sA = self.sA
            sB = self.sB
            sC = self.sC
            obvod = sA + sB + sC
            s = obvod / 2
            obsah = math.sqrt(s * (s - sA) * (s - sB) * (s - sC))
            cosA = (sB ** 2 + sC ** 2 - sA ** 2) / (2 * sB * sC)
            cosB = (sA ** 2 + sC ** 2 - sB ** 2) / (2 * sA * sC)
            cosC = (sA ** 2 + sB ** 2 - sC ** 2) / (2 * sA * sB)
            uA = round(math.degrees(math.acos(cosA)), 2)
            uB = round(math.degrees(math.acos(cosB)), 2)
            uC = round(math.degrees(math.acos(cosC)), 2)
            obsah = round(obsah, 2)
            if uA == uB and uB == uC:
                return {"obsah": str(obsah) + "cm\u00B2",
                        "obvod": str(obvod) + "cm",
                        "úhel \u03B1, \u03B2, \u03B3": str(uA) + "°",
                        "typ trojúhelníku": "rovnostranný"}
            elif uA == uB:
                return {"obsah": str(obsah) + "cm\u00B2",
                        "obvod": str(obvod) + "cm",
                        "úhel \u03B1, \u03B2": str(uA) + "°",
                        "úhel \u03B3": str(uC) + "°",
                        "typ trojúhelníku": "rovnoramenný"}
            elif uA == uC:
                return {"obsah": str(obsah) + "cm\u00B2",
                        "obvod": str(obvod) + "cm",
                        "úhel \u03B1, \u03B3": str(uA) + "°",
                        "úhel \u03B2": str(uB) + "°",
                        "typ trojúhelníku": "rovnoramenný"}
            elif uB == uC:
                return {"obsah": str(obsah) + "cm\u00B2",
                        "obvod": str(obvod) + "cm",
                        "úhel \u03B1": str(uA) + "°",
                        "úhel \u03B2, \u03B3": str(uB) + "°",
                        "typ trojúhelníku": "rovnoramenný"}
            elif uA == 90 or uB == 90 or uC == 90:
                return {"obsah": str(obsah) + "cm\u00B2",
                        "obvod": str(obvod) + "cm",
                        "úhel \u03B1": str(uA) + "°",
                        "úhel \u03B2": str(uB) + "°",
                        "úhel \u03B3": str(uC) + "°",
                        "typ trojúhelníku": "pravoúhlý"}
            else:
                return {"obsah": str(obsah) + "cm\u00B2",
                        "obvod": str(obvod) + "cm",
                        "úhel \u03B1": str(uA) + "°",
                        "úhel \u03B2": str(uB) + "°",
                        "úhel \u03B3": str(uC) + "°",
                        "typ trojúhelníku": "obecný"}

        else:
            out = "Nejedná se o trojúhelník."
            out += " Součet dvou stran musí být větší než stranatřetí."
            return out


sss = Tris(3, 4, 15)
print(sss)
