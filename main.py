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
            self.tris_sss()

    def is_tris(self):
        if self.sA + self.sB > self.sC and self.sA + self.sC > self.sB and self.sB + self.sC > self.sA:
            return True
        else:
            return False

    def tris_sss(self):
        if self.is_tris():
            self.obvod = self.sA + self.sB + self.sC
            self.cosA = (self.sB ** 2 + self.sC ** 2 - self.sA ** 2) / (2 * self.sB * self.sC)
            self.cosB = (self.sA ** 2 + self.sC ** 2 - self.sB ** 2) / (2 * self.sA * self.sC)
            self.cosC = (self.sA ** 2 + self.sB ** 2 - self.sC ** 2) / (2 * self.sA * self.sC)
            self.uA = round(math.degrees(math.acos(self.cosA)), 2)
            self.uB = round(math.degrees(math.acos(self.cosB)), 2)
            self.uC = round(math.degrees(math.acos(self.cosC)), 2)
            self.s = self.obvod / 2
            self.obsah = math.sqrt(self.s * (self.s - self.sA) * (self.s - self.sB) * (self.s - self.sC))
            self.trojuhelnik = {"obsah" : str(self.obsah) + "cm\u00B2",
                           "obvod" : str(self.obvod) + "cm",
                           "úhel \u03B1" : str(self.uA) + "°",
                           "úhel \u03B2" : str(self.uB) + "°",
                           "úhel \u03B3" : str(self.uC) + "°"}
            return self.trojuhelnik
        else:
            return "Nejedná se o trojúhelník"



sss =tris(3, 4, 15)
print(str(sss))
