# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:53:37 2020.

@author: Tomas Adamek
"""
import math
import re
import tkinter as tk


def toNumber(value):
    """
    Funkce umožnující vložení do inputu matematické operátory.

    V případě že dostane prázdný string vloží do něj nulu. smaže všechn
    nežádoucí znaky. Změní desetinou čárku na opovídající tvar.
    """
    if value == "":
        value = "0"
    value = "(" + value + ")+0"
    value = value.replace(",", ".")
    value = re.sub(r'[\w ][^sqrt()0-9+./*-]', '', value)
    value = value.replace("sqrt", "math.sqrt")
    value = eval(value)
    return value


class Uprava_jednotek():
    """Třída pro úpravu inputu pro logiku."""

    def prevod_delky(self):
        """Metoda pro prevod delek na jednotnou variantu."""
        if self.unsA != "" and self.unsB != "" and self.unsC != "":
            (self.unsA, self.unsB,
             self.sA, self.sB) = self.dve_strany(self.unsA, self.unsB,
                                                 self.sA, self.sB)
            if self.unsA != self.unsC:
                (self.unsA, self.unsC,
                 self.sA, self.sC) = self.dve_strany(self.unsA, self.unsC,
                                                     self.sA, self.sC)
                (self.unsB, self.unsC,
                 self.sB, self.sC) = self.dve_strany(self.unsB, self.unsC,
                                                     self.sB, self.sC)
        elif self.unsA != "" and self.unsB != "":
            (self.unsA, self.unsB,
             self.sA, self.sB) = self.dve_strany(self.unsA, self.unsB,
                                                 self.sA, self.sB)
        elif self.unsA != "" and self.unsC != "":
            (self.unsA, self.unsC,
             self.sA, self.sC) = self.dve_strany(self.unsA, self.unsC,
                                                 self.sA, self.sC)
        elif self.unsB != "" and self.unsC != "":
            (self.unsB, self.unsC,
             self.sB, self.sC) = self.dve_strany(self.unsB, self.unsC,
                                                 self.sB, self.sC)
        elif self.unsA == "" and self.unsB == "" and self.unsC != "":
            self.unitD = self.unsC
        elif self.unsA == "" and self.unsC == "" and self.unsB != "":
            self.unitD = self.unsB
        elif self.unsB == "" and self.unsC == "" and self.unsA != "":
            self.unitD = self.unsA
        else:
            self.unitD = "m"

    def dve_strany(self, strana1, strana2, s1, s2):
        """Prevadí dve delky na stejnou jednotku."""
        if strana1 != strana2:
            strana1 = self.delka_to_int(strana1)
            strana2 = self.delka_to_int(strana2)
            if strana1 > strana2:
                x = strana1 - strana2
                for y in range(x):
                    s1 *= 10
                self.unitD = self.int_to_delka(strana2)
            elif strana1 < strana2:
                x = strana2 - strana1
                for y in range(x):
                    s2 *= 10
                self.unitD = self.int_to_delka(strana1)
            strana1 = self.unitD
            strana2 = self.unitD
        else:
            self.unitD = self.int_to_delka(strana1)
        return strana1, strana2, s1, s2

    def delka_to_int(self, myunit):
        """Prevede text na cislo."""
        if myunit == "mm":
            myunit = 1
        elif myunit == "cm":
            myunit = 2
        elif myunit == "dm":
            myunit = 3
        elif myunit == "m":
            myunit = 4
        elif myunit == "km":
            myunit = 7
        elif myunit == "":
            myunit = 0
        return myunit

    def int_to_delka(self, myunit):
        """Prevede cisla na text."""
        if myunit == 1:
            myunit = "mm"
        elif myunit == 2:
            myunit = "cm"
        elif myunit == 3:
            myunit = "dm"
        elif myunit == 4:
            myunit = "m"
        elif myunit == 7:
            myunit = "km"
        elif myunit == 0:
            myunit == ""
        return myunit

    def to_rad(self, uhel1, u1):
        """Převede uhly na radiany."""
        if uhel1 != "rad":
            uhel1 = self.uhel_to_int(uhel1)
            if uhel1 == 3:
                u1 *= math.pi
                uhel1 = 2
            elif uhel1 == 1:
                u1 = math.radians(u1)
                uhel1 = 2
            uhel1 = self.int_to_uhel(uhel1)
        return u1

    def uhel_to_int(self, myunit):
        """Zmení text na čísla."""
        if myunit == "\xb0":
            myunit = 1
        elif myunit == "rad":
            myunit = 2
        elif myunit == "\u03C0 rad":
            myunit = 3
        elif myunit == "":
            myunit = 0
        return myunit

    def int_to_uhel(self, myunit):
        """Zmení čísla zpet na text."""
        if myunit == 1:
            myunit = "\xb0"
        elif myunit == 2:
            myunit = "rad"
        elif myunit == 3:
            myunit = "\u03C0 rad"
        elif myunit == 0:
            myunit = ""
        return myunit


class Tris(Uprava_jednotek):
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

    def __init__(self, hodnoty):
        """
        Konsruktor.

        Vytvori promene pro metody a rozhodne jakou metodu vyuzit
        pro vypocitani dalsich promenych
        """
        self.unsA = hodnoty[0][1]
        self.unsB = hodnoty[1][1]
        self.unsC = hodnoty[2][1]
        self.unuA = hodnoty[3][1]
        self.unuB = hodnoty[4][1]
        self.unuC = hodnoty[5][1]
        self.sA = toNumber(hodnoty[0][0])
        self.sB = toNumber(hodnoty[1][0])
        self.sC = toNumber(hodnoty[2][0])
        self.uA = self.to_rad(self.unuA, toNumber(hodnoty[3][0]))
        self.uB = self.to_rad(self.unuB, toNumber(hodnoty[4][0]))
        self.uC = self.to_rad(self.unuC, toNumber(hodnoty[5][0]))
        self.prevod_delky()
        self.unitU = "rad"
        if ((self.uA + self.uB < math.pi) or (self.uA + self.uC < math.pi) or
                (self.uB + self.uC < math.pi)):
            if self.sA > 0 and self.sB > 0 and self.sC > 0:
                self.result = self.tris_sss()
            elif ((self.sA > 0 and self.sB > 0 or self.sA > 0 and self.sC > 0 or
                  self.sB > 0 and self.sC > 0) and (self.uA > 0 or self.uB > 0 or
                                                    self.uC > 0)):
                self.result = self.tris_sus()
            elif ((self.uA > 0 and self.uB > 0 or self.uA > 0 and self.uC > 0 or
                  self.uB > 0 and self.uC > 0) and (self.sA > 0 or self.sB > 0 or
                                                    self.sC > 0)):
                self.result = self.tris_usu()
        else:
            self.result = self.output()

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
        uA = self.uA
        uB = self.uB
        uC = self.uC
        if sA > 0 and sB > 0 and sC > 0:
            if sA + sB > sC and sA + sC > sB and sB + sC > sA:
                return True
            else:
                return False
        elif not (uA + uB < math.pi or uA + uC < math.pi or uB + uC < math.pi):
            return True
        else:
            return False

    def cos_veta(self, arg):
        """
        Cosinova veta pro vypocet uhlu ze stran.

        arg = <str> uA / uB / uC / (zadané se počítá)
        """
        sA = self.sA
        sB = self.sB
        sC = self.sC
        if arg == "uA":
            return math.acos((sB ** 2 + sC ** 2 - sA ** 2) / (2 * sB * sC))
        elif arg == "uB":
            return math.acos((sA ** 2 + sC ** 2 - sB ** 2) / (2 * sA * sC))
        elif arg == "uC":
            return math.acos((sA ** 2 + sB ** 2 - sC ** 2) / (2 * sA * sB))

        else:
            print("argument musí být 'uA', 'uB', nebo 'uC'")

    def sin_veta(self, arg):
        """
        Sinova veta pro vypocet uhlu ze stran.

        arg = <str> uA / uB / uC / sA / sB / sC (zadané se počítá)
        """
        sA = self.sA
        sB = self.sB
        sC = self.sC
        uA = self.uA
        uB = self.uB
        uC = self.uC
        if arg == "uA":
            if sB > 0 and uB > 0 and sA > 0:
                return math.asin(sA / (sB / math.sin(uB)))
            elif sC > 0 and uC > 0 and sA > 0:
                return math.asin(sA / (sC / math.sin(uC)))
        elif arg == "uB":
            if sA > 0 and uA > 0 and sB > 0:
                return math.asin(sB / (sA / math.sin(uA)))
            elif sC > 0 and uC > 0 and sB > 0:
                return math.asin(sB / (sC / math.sin(uC)))
        elif arg == "uC":
            if sA > 0 and uA > 0 and sC > 0:
                return math.asin(sC / (sA / math.sin(sA)))
            elif sB > 0 and uB > 0 and sC > 0:
                return math.asin(sC / (sB / math.sin(uB)))
        elif arg == "sA":
            if sB > 0:
                return (sB * (math.sin(uA) / math.sin(uB)))
            elif sC > 0:
                return (sC * (math.sin(uA) / math.sin(uC)))
        elif arg == "sB":
            if sA > 0:
                return (sA * (math.sin(uB) / math.sin(uA)))
            elif sC > 0:
                return (sC * (math.sin(uB) / math.sin(uC)))
        elif arg == "sC":
            if sA > 0:
                return (sA * (math.sin(uC) / math.sin(uA)))
            elif sB > 0:
                return (sB * (math.sin(uC) / math.sin(uB)))
        else:
            print("argument musí být 'uA', 'uB', 'uC', 'sA', 'sB', nebo 'sC'")

    def tris_usu(self):
        """Vypocita strany a uhly podle vety usu."""
        if self.uA > 0 and self.uB > 0:
            self.uC = math.pi - (self.uB + self.uA)
        elif self.uA > 0 and self.uC > 0:
            self.uB = math.pi - (self.uA + self.uC)
        elif self.uB > 0 and self.uC > 0:
            self.uA = math.pi - (self.uB + self.uC)
        if self.sA > 0:
            self.sB = self.sin_veta("sB")
            self.sC = self.sin_veta("sC")
        elif self.sB > 0:
            self.sA = self.sin_veta("sA")
            self.sC = self.sin_veta("sC")
        elif self.sC > 0:
            self.sA = self.sin_veta("sA")
            self.sB = self.sin_veta("sB")
        return self.output()

    def tris_sus(self):
        """Vypocita strany a uhly podle vety sus."""
        sA = self.sA
        sB = self.sB
        sC = self.sC
        uA = self.uA
        uB = self.uB
        uC = self.uC
        # zakladni cosinové věty
        if sB > 0 and sC > 0 and uA > 0:
            self.sA = math.sqrt(sB ** 2 + sC ** 2
                                - (2 * sB * sC * math.cos(uA)))
            self.uB = self.cos_veta("uB")
            self.uC = self.cos_veta("uC")
        elif sB > 0 and sC > 0 and uB > 0:
            self.uC = self.sin_veta("uC")
            self.uA = math.pi - (self.uB + self.uC)
            self.sA = math.sqrt(sB ** 2 + sC ** 2
                                - (2 * sB * sC * math.cos(self.uA)))
        elif sB > 0 and sC > 0 and uC > 0:
            self.uB = self.sin_veta("uB")
            self.uA = math.pi - (self.uB + self.uC)
            self.sA = math.sqrt(sB ** 2 + sC ** 2
                                - (2 * sB * sC * math.cos(self.uA)))
        elif sA > 0 and sC > 0 and uA > 0:
            self.uC = self.sin_veta("uC")
            self.uB = math.pi - (self.uA + self.uC)
            self.sB = self.sB = math.sqrt(sA ** 2 + sC ** 2
                                          - (2 * sA * sC * math.cos(self.uB)))
        # zakladni cosinové věty
        elif sA > 0 and sC > 0 and uB > 0:
            self.sB = math.sqrt(sA ** 2 + sC ** 2
                                - (2 * sA * sC * math.cos(uB)))
            self.uA = self.cos_veta("uA")
            self.uC = self.cos_veta("uC")
        elif sA > 0 and sC > 0 and uC > 0:
            self.uA = self.sin_veta("uA")
            self.uB = math.pi - (self.uA + self.uC)
            self.sB = math.sqrt(sA ** 2 + sC ** 2
                                - (2 * sA * sC * math.cos(self.uB)))
        elif sA > 0 and sB > 0 and uA > 0:
            self.uB = self.sin_veta("uB")
            self.uC = math.pi - (self.uA + self.uB)
            self.sC = math.sqrt(sA ** 2 + sB ** 2
                                - (2 * sA * sC * math.cos(self.uC)))
        elif sA > 0 and sB > 0 and uB > 0:
            self.uA = self.sin_veta("uA")
            self.uC = math.pi - (self.uA + self.uB)
            self.sC = math.sqrt(sA ** 2 + sB ** 2
                                - (2 * sA * sC * math.cos(self.uC)))
        # zakladni cosinové věty
        elif sA > 0 and sB > 0 and uC > 0:
            self.sC = math.sqrt(sA ** 2 + sB ** 2
                                - (2 * sA * sC * math.cos(uC)))
            self.uA = self.cos_veta("uA")
            self.uB = self.cos_veta("uB")
        return self.output()

    def tris_sss(self):
        """Výpočet podle vetey sss."""
        self.uA = self.cos_veta("uA")
        self.uB = self.cos_veta("uB")
        self.uC = self.cos_veta("uC")
        return self.output()

    def output(self):
        """Výstup z třídy."""
        tmp = self.delka_to_int(self.unitD)
        if self.is_tris():
            if self.sA < 1 and self.sB < 1 and self.sC < 1:
                while True:
                    if (tmp == 7 and self.sA < 1 and self.sB < 1 and
                            self.sC < 1):
                        tmp -= 3
                        self.sA *= 1000
                        self.sB *= 1000
                        self.sC *= 1000
                        self.unitD = self.int_to_delka(tmp)
                    elif (tmp > 1 and tmp <= 4 and self.sA < 1 and
                            self.sB < 1 and self.sC < 1):
                        tmp -= 1
                        self.sA *= 10
                        self.sB *= 10
                        self.sC *= 10
                        self.unitD = self.int_to_delka(tmp)
                    else:
                        break
            elif ((self.sA % 10 and isinstance(self.sA, int)) or
                  (self.sB % 10 and isinstance(self.sB, int)) or
                  (self.sC % 10 and isinstance(self.sC, int))):
                while True:
                    if tmp < 4 and tmp > 1: 
                        if ((self.sA % 10 and isinstance(self.sA, int)) and
                              (self.sB % 10 and isinstance(self.sB, int)) and
                              (self.sC % 10 and isinstance(self.sC, int))):
                            tmp += 1
                            self.sA /= 10
                            self.sB /= 10
                            self.sC /= 10
                            self.unitD = self.int_to_delka(tmp)
                    else:
                        break
            sA = self.sA
            sB = self.sB
            sC = self.sC
            uA = round(self.uA, 5)
            uB = round(self.uB, 5)
            uC = round(self.uC, 5)
            uAd = round(math.degrees(self.uA), 5)
            uBd = round(math.degrees(self.uB), 5)
            uCd = round(math.degrees(self.uC), 5)
            obvod = sA + sB + sC
            s = obvod / 2
            obsah = round(math.sqrt(s * (s - sA) * (s - sB) * (s - sC)), 2)
            obvod = round(obvod, 5)
            sA = round(sA, 5)
            sB = round(sB, 5)
            sC = round(sC, 5)
            tpTris = {0: "typ – rovnostranný",
                      1: "typ – rovnoramenný, pravoúhlý",
                      2: "typ – rovnoramenný",
                      3: "typ – pravoúhlý",
                      4: "typ – obecný"}
            out  = {0: "strana a – " + str(sA) + self.unitD,
                    1: "strana b – " + str(sB) + self.unitD,
                    2: "strana c – " + str(sC) + self.unitD,
                    3: "úhel \u03B1 – " + str(uA) + self.unitU,
                    4: "úhel \u03B2 – " + str(uB) + self.unitU,
                    5: "úhel \u03B3 – " + str(uC) + self.unitU,
                    6: "obvod  – " + str(obvod) + self.unitD,
                    7: "obsah – " + str(obsah) + self.unitD + "\u00B2"}
            if uA == uB and uB == uC:
                out[8] = tpTris[0]
            elif ((uA == uB and uCd == 90) or (uA == uC and uBd ==90) 
                  or (uB == uC and uAd == 90)):
                out[8] = tpTris[1]
            elif uA == uB or uA == uC or uB == uC:
                out[8] = tpTris[2]
            elif uAd == 90 or uBd == 90 or uCd == 90:
                out[8] = tpTris[3]
            else:
                out[8] = tpTris[4]
        else:
            out = "Nejedná se o trojúhelník.\n"
            out += "Součet dvou stran musí být větší než strana třetí.\n"
            out += "Součet dvou úhlů musí být menší než 360\xb0 nebo "
            out += "\u03C0 rad."
        return out

class Gui(tk.Tk):
    """Class pro gui."""

    def __init__(self):
        """Konstruktor základní struktury."""
        self.app = tk.Tk()
        self.app.configure(bg="#1d1d1d")
        self.app.title("Výpočet troúhelníků")
        self.app.columnconfigure(0, weight=2)
        self.app.columnconfigure(1, weight=2)
        self.app.columnconfigure(2, weight=2)
        self.app.columnconfigure(3, weight=2)
        self.app.columnconfigure(4, weight=2)
        self.app.columnconfigure(5, weight=2)
        self.app.minsize(450, 577)
        self.app.maxsize(450, 577)
        self.app.option_add("*font", "Helvetica 10 bold")
        self.canvas = tk.Canvas()
        self.nazvy = {1: "Strana a",
                      2: "Strana b",
                      3: "Strana c",
                      4: "Úhel \u03B1",
                      5: "Úhel \u03B2",
                      6: "Úhel \u03B3"}
        self.issA = tk.BooleanVar()
        self.issA.set(False)
        self.issB = tk.BooleanVar()
        self.issB.set(False)
        self.issC = tk.BooleanVar()
        self.issC.set(False)
        self.isuA = tk.BooleanVar()
        self.isuA.set(False)
        self.isuB = tk.BooleanVar()
        self.isuB.set(False)
        self.isuC = tk.BooleanVar()
        self.isuC.set(False)
        self.count = 0
        self.checkbox_render()
        self.value_render()
        self.image_render()
        self.app.mainloop()

    def checkbox_render(self):
        """Stylování a vykreslování checkboxu."""
        self.chbsA = tk.Checkbutton(self.app, text=self.nazvy[1],
                                    variable=self.issA,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbsA.grid(row=0, column=0, sticky="W")
        self.chbsB = tk.Checkbutton(self.app, text=self.nazvy[2],
                                    variable=self.issB,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbsB.grid(row=0, column=1, sticky="W")
        self.chbsC = tk.Checkbutton(self.app, text=self.nazvy[3],
                                    variable=self.issC,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbsC.grid(row=0, column=2, sticky="W")
        self.chbuA = tk.Checkbutton(self.app, text=self.nazvy[4],
                                    variable=self.isuA,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbuA.grid(row=1, column=0, sticky="W")
        self.chbuB = tk.Checkbutton(self.app, text=self.nazvy[5],
                                    variable=self.isuB,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbuB.grid(row=1, column=1, sticky="W")
        self.chbuC = tk.Checkbutton(self.app, text=self.nazvy[6],
                                    variable=self.isuC,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbuC.grid(row=1, column=2, sticky="W")

    def count_of_true(self):
        """Bere hodnoty z checkboxů a počítá kolik jich je True."""
        self.count = 0
        if self.issA.get():
            self.count += 1
        if self.issB.get():
            self.count += 1
        if self.issC.get():
            self.count += 1
        if self.isuA.get():
            self.count += 1
        if self.isuB.get():
            self.count += 1
        if self.isuC.get():
            self.count += 1
        self.value_render()
        self.image_render()
        self.downer_panel_render()
        self.input_render_choice()

    def value_render(self):
        """Vypisuje pokyni."""
        self.stav = {0: "Vyberte, které veličiny zadáte.\n",
                     1: "Pokracujte ve vybírání. Vyberte další {} "
                     "veličiny.\n".format(self.count*-1+3),
                     2: "Perfektní! Více veličin nepotřebuji.\n"}
        if self.count == 0:
            self.instrukce = tk.Label(self.app, text=self.stav[0],
                                      bg="#1d1d1d", fg="white",
                                      anchor="w", height=3)
        elif self.count > 0 and self.count < 3:
            self.instrukce = tk.Label(self.app, text=self.stav[1],
                                      bg="#1d1d1d", fg="white",
                                      anchor="w", height=3)
        else:
            self.instrukce = tk.Label(self.app, text=self.stav[2],
                                      bg="#1d1d1d", fg="white",
                                      anchor="w", height=3)
        self.instrukce.grid(row=2, column=0, columnspan=3, sticky="ew")
        self.turn_off_checkbox()

    def turn_off_checkbox(self):
        """Vypíná checkboxy po té co jsou vybrané 3, nebo dva uhly."""
        
        if self.count == 3:
            if not self.issA.get():
                self.chbsA.configure(state="disabled")
            if not self.issB.get():
                self.chbsB.configure(state="disabled")
            if not self.issC.get():
                self.chbsC.configure(state="disabled")
            if not self.isuA.get():
                self.chbuA.configure(state="disabled")
            if not self.isuB.get():
                self.chbuB.configure(state="disabled")
            if not self.isuC.get():
                self.chbuC.configure(state="disabled")
        elif self.isuA.get() and self.isuB.get():
            self.chbuC.configure(state="disabled")
            self.chbsA.configure(state="normal")
            self.chbsB.configure(state="normal")
            self.chbsC.configure(state="normal")
        elif self.isuA.get() and self.isuC.get():
            self.chbuB.configure(state="disabled")
            self.chbsA.configure(state="normal")
            self.chbsB.configure(state="normal")
            self.chbsC.configure(state="normal")
        elif self.isuB.get() and self.isuC.get():
            self.chbuA.configure(state="disabled")
            self.chbsA.configure(state="normal")
            self.chbsB.configure(state="normal")
            self.chbsC.configure(state="normal")
        else:
            self.chbsA.configure(state="normal")
            self.chbsB.configure(state="normal")
            self.chbsC.configure(state="normal")
            self.chbuA.configure(state="normal")
            self.chbuB.configure(state="normal")
            self.chbuC.configure(state="normal")

    def image_render(self):
        """Vykresluje interaktivní obrázek trojúhelníku."""
        myhelp = "Do polí je možné vkládat matematické operátory.\n"
        myhelp += "\u221a = sqrt(zde cislo),\n\u00d7 = * ,\n\u00f7 = /"
        trImg = tk.Canvas(self.app, bg="#1d1d1d", width=450, height=445,
                          highlightbackground="#1d1d1d")
        trImg.grid(row=3, column=0, columnspan=3, sticky='we')
        trImg.create_text(35, 360, anchor="w", text="A", fill="white",
                          font=("Helvetica", "16", "bold"))
        trImg.create_text(405, 360, anchor="w", text="B", fill="white",
                          font=("Helvetica", "16", "bold"))
        trImg.create_text(225, 25, anchor="center", text="C", fill="white",
                          font=("Helvetica", "16", "bold"))
        trImg.create_text(225, 360, anchor="center", text="strana c",
                          fill="white", font=("Helvetica", "12", "bold"))
        trImg.create_text(120, 185, anchor="center", text="strana b",
                          angle=60, fill="white",
                          font=("Helvetica", "12", "bold"))
        trImg.create_text(330, 185, anchor="center", text="strana a",
                          angle=-60, fill="white",
                          font=("Helvetica", "12", "bold"))
        trImg.create_text(105, 310, anchor="center", text="\u03B1",
                          fill="white", font=("Helvetica", "12", "bold"))
        trImg.create_text(345, 310, anchor="center", text="\u03B2",
                          fill="white", font=("Helvetica", "12", "bold"))
        trImg.create_text(225, 105, anchor="center", text="\u03B3",
                          fill="white", font=("Helvetica", "12", "bold"))
        uaA = trImg.create_arc(0, 293.109, 100, 393.109, start=0, extent=60,
                               outline="white", width=1.5)
        uaB = trImg.create_arc(350, 293.109, 450, 393.109, start=120,
                               extent=60, outline="white", width=1.5)
        uaC = trImg.create_arc(175, -10, 275, 90, start=240,
                               extent=60, outline="white", width=1.5)
        slC = trImg.create_line(50, 343.109, 400, 343.109, fill="white",
                                width=3)
        slA = trImg.create_line(400, 343.109, 225, 40, fill="white", width=3)
        slB = trImg.create_line(225, 40, 50, 343.109, fill="white", width=3)
        trImg.create_text(40, 420, anchor="w", text=myhelp, fill="yellow",
                          font=("Helvetica", "10", "bold"))
        if self.issA.get():
            trImg.itemconfig(slA, fill="green")
        if self.issB.get():
            trImg.itemconfig(slB, fill="green")
        if self.issC.get():
            trImg.itemconfig(slC, fill="green")
        if self.isuA.get():
            trImg.itemconfig(uaA, fill="green")
        if self.isuB.get():
            trImg.itemconfig(uaB, fill="green")
        if self.isuC.get():
            trImg.itemconfig(uaC, fill="green")

    def input_render(self, var, txt, values, myrow, mycolumn, unit):
        """
        generovaní inputu.

        var = proměná pro uložení hodnoty, txt = nadpisek pro vkládání.
        values = 0 je délka, 1 jsou uhly, myrow = radek, mycolumn = pocatecni
        sloupec
        """
        tk.Label(self.frame, text=txt, bg="#1d1d1d", fg="white", bd=5,
                 anchor="n").grid(row=myrow, column=mycolumn, sticky="w")
        tk.Spinbox(self.frame, bg="green", fg="white", from_=0.1,
                   to=10000, buttonbackground="#1d1d1d", increment=0.05,
                   width=30, textvariable=var
                   ).grid(row=myrow, sticky="w", column=mycolumn+1)
        if values == 0:
            ol = ("mm", "cm", "dm", "m", "km")
            unit.set("m")
            self.om = tk.OptionMenu(self.frame, unit, *ol)
            self.om.config(bg="#1d1d1d", bd=5, fg="white", relief="flat",
                           highlightthickness=0, width=5,
                           activebackground="green", height=1,
                           activeforeground="white")
            self.om["menu"].config(bg="#1d1d1d", fg="white",
                                   activebackground="green",
                                   activeforeground="white")
            self.om.grid(row=myrow, column=mycolumn+2, sticky="w", pady=2)

        else:
            ol = ("\xb0", "rad", "\u03C0 rad")
            unit.set("\xb0")
            self.om = tk.OptionMenu(self.frame, unit, *ol)
            self.om.config(bg="#1d1d1d", bd=5, fg="white", relief="flat",
                           highlightthickness=0, width=5,
                           activebackground="green", height=1,
                           activeforeground="white")
            self.om["menu"].config(bg="#1d1d1d", fg="white",
                                   activebackground="green",
                                   activeforeground="white")
            self.om.grid(row=myrow, column=mycolumn+2, sticky="w", pady=2)
        if self.count == 3:
            tk.Button(self.frame, text="Vypočítej", bg="green", fg="white",
                      padx=190, pady=15, relief="flat",
                      activebackground="#7daa7d", activeforeground="white",
                      command=self.get_values, state="normal"
                      ).grid(row=3, column=3, columnspan=3, sticky="w")
        else:
            tk.Button(self.frame, text="Vypočítej", bg="#2d2d2d", fg="white",
                      padx=190, pady=15, relief="flat", state="disabled",
                      command=self.get_values
                      ).grid(row=3, column=3, columnspan=3, sticky="w")

    def downer_panel_render(self):
        """Vykresluje panel pod nákresem trojúhelníku."""
        self.frame = tk.Frame(self.app, width=450, bg="#1d1d1d")
        self.frame.grid(column=0, row=4, columnspan=6, rowspan=5,
                        sticky="wn")
        if self.count > 0:
            self.app.minsize(450, 735)
            self.app.maxsize(450, 735)

    def blank(self, myrow, mycolumn):
        """Vykresluje prázdné místonamísto inputu."""
        tk.Label(self.frame, width=55, bg="#1d1d1d", height=2
                 ).grid(row=myrow, column=mycolumn, columnspan=6, sticky="we")

    def input_render_choice(self):
        """Vykresluje input na obrazovku."""
        self.sA = tk.StringVar()
        self.sB = tk.StringVar()
        self.sC = tk.StringVar()
        self.uA = tk.StringVar()
        self.uB = tk.StringVar()
        self.uC = tk.StringVar()
        self.unsA = tk.StringVar()
        self.unsB = tk.StringVar()
        self.unsC = tk.StringVar()
        self.unuA = tk.StringVar()
        self.unuB = tk.StringVar()
        self.unuC = tk.StringVar()
        if self.issA.get():
            self.mysA = self.input_render(self.sA, "strana a", 0, 0, 3,
                                          self.unsA)
            if self.issB.get():
                self.input_render(self.sB, "strana b", 0, 1, 3, self.unsB)
                if self.issC.get():
                    self.input_render(self.sC, "strana c", 0, 2, 3, self.unsC)
                elif self.isuA.get():
                    self.input_render(self.uA, "úhel \u03B1", 1, 2, 3,
                                      self.unuA)
                elif self.isuB.get():
                    self.input_render(self.uB, "úhel \u03B2", 1, 2, 3,
                                      self.unuB)
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.issC.get():
                self.input_render(self.sC, "strana c", 0, 1, 3, self.unsC)
                if self.isuA.get():
                    self.input_render(self.uA, "úhel \u03B1", 1, 2, 3,
                                      self.unuA)
                elif self.isuB.get():
                    self.input_render(self.uB, "úhel \u03B2", 1, 2, 3,
                                      self.unuB)
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuA.get():
                self.input_render(self.uA, "úhel \u03B1", 1, 1, 3, self.unuA)
                if self.isuB.get():
                    self.input_render(self.uB, "úhel \u03B2", 1, 2, 3,
                                      self.unuB)
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3,
                                  self.unuB)
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuC.get():
                self.input_render(self.uC, "úhel \u03B3", 1, 1, 3,
                                  self.unuC)
                self.blank(2, 3)
            else:
                self.blank(1, 3)
                self.blank(2, 3)
        elif self.issB.get():
            self.input_render(self.sB, "strana b", 0, 0, 3,
                              self.unsB)
            if self.issC.get():
                self.input_render(self.sC, "strana c", 0, 1, 3,
                                  self.unsC)
                if self.isuA.get():
                    self.input_render(self.uA, "úhel \u03B1", 1, 2, 3,
                                      self.unuA)
                elif self.isuB.get():
                    self.input_render(self.uB, "úhel \u03B2", 1, 2, 3,
                                      self.unuB)
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuA.get():
                self.input_render(self.uA, "úhel \u03B1", 1, 1, 3, self.unuA)
                if self.isuB.get():
                    self.input_render(self.uB, "úhel \u03B2", 1, 2, 3,
                                      self.unuB)
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3, self.unuB)
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuC.get():
                self.input_render(self.uC, "úhel \u03B3", 1, 1, 3, self.unuC)
                self.blank(2, 3)
            else:
                self.blank(1, 3)
                self.blank(2, 3)
        elif self.issC.get():
            self.input_render(self.sC, "strana c", 0, 0, 3, self.unsC)
            if self.isuA.get():
                self.input_render(self.uA, "úhel \u03B1", 1, 1, 3,
                                  self.unuA)
                if self.isuB.get():
                    self.input_render(self.uB, "úhel \u03B2", 1, 2, 3,
                                      self.unuB)
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3, self.unuB)
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuC.get():
                self.input_render(self.uC, "úhel \u03B3", 1, 1, 3,
                                  self.unuC)
                self.blank(2, 3)
            else:
                self.blank(1, 3)
                self.blank(2, 3)
        elif self.isuA.get():
            self.input_render(self.uA, "úhel \u03B1", 1, 0, 3, self.unuA)
            if self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3, self.unuB)
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                else:
                    self.blank(2, 3)
            elif self.isuC.get():
                self.input_render(self.uC, "úhel \u03B3", 1, 1, 3, self.unuC)
                self.blank(2, 3)
            else:
                self.blank(1, 3)
                self.blank(2, 3)
        elif self.isuB.get():
            self.input_render(self.uB, "úhel \u03B2", 1, 0, 3, self.unuB)
            if self.isuC.get():
                self.input_render(self.uC, "úhel \u03B3", 1, 1, 3, self.unuC)
                self.blank(2, 3)
            else:
                self.blank(1, 3)
                self.blank(2, 3)
        elif self.isuC.get():
            self.input_render(self.uC, "úhel \u03B3", 1, 0, 3, self.unuC)
            self.blank(1, 3)
            self.blank(2, 3)
        else:
            self.blank(0, 3)
            self.blank(1, 3)
            self.blank(2, 3)

    def get_values(self):
        """Ziska hodnoty z inputu a pošle je logice."""
        myOutput = Tris({0: (self.sA.get(), self.unsA.get()),
                         1: (self.sB.get(), self.unsB.get()),
                         2: (self.sC.get(), self.unsC.get()),
                         3: (self.uA.get(), self.unuA.get()),
                         4: (self.uB.get(), self.unuB.get()),
                         5: (self.uC.get(), self.unuC.get())})
        print(myOutput)


if __name__ == "__main__":
    Gui()
