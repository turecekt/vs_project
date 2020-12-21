# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:53:37 2020.

@author: Tomas Adamek
"""
import math
import tkinter as tk
from tkinter import ttk


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


class Uprava_jednotek():
    def __init__(self, sA, sB, sC, uA, uB, uC, unsA, unsB, unsC, unuA, unuB,
                 unuC):
        self.sA = sA
        self.sB = sB
        self.sC = sC
        self.uA = uA
        self.uB = uB
        self.uC = uC
        self.unsA = unsA
        self.unsB = unsB
        self.unsC = unsC
        self.unuA = unuA
        self.unuB = unuB
        self.unuC = unuC
        print(self.sA)

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
        self.app.minsize(450, 502)
        self.app.maxsize(450, 502)
        self.app.option_add("*font", "Helvetica 10 bold")
        self.canvas = tk.Canvas()
        self.nazvy = {1: "Strana a",
                      2: "Strana b",
                      3: "Strana c",
                      4: "Úhel \u03B1",
                      5: "Úhel \u03B2",
                      6: "Úhel \u03B3"}
        
        # Definice proměnných pro metodu checkbox_render()
        # je strana A vybraná?
        self.issA = tk.BooleanVar()
        self.issA.set(False)
        # je strana B vybraná?
        self.issB = tk.BooleanVar()
        self.issB.set(False)
        # je strana C vybraná?
        self.issC = tk.BooleanVar()
        self.issC.set(False)
        # je úhel A vybraný?
        self.isuA = tk.BooleanVar()
        self.isuA.set(False)
        # je úhel B vybraný?
        self.isuB = tk.BooleanVar()
        self.isuB.set(False)
        # je úhel C vybraný?
        self.isuC = tk.BooleanVar()
        self.isuC.set(False)
        # proměná pro metodu count_of_true()
        self.count = 0
        # volání metody checkbox_render()
        self.sA = tk.DoubleVar()
        self.sB = tk.DoubleVar()
        self.sC = tk.DoubleVar()
        self.uA = tk.DoubleVar()
        self.uB = tk.DoubleVar()
        self.uC = tk.DoubleVar()
        self.unsA = tk.StringVar()
        self.unsB = tk.StringVar()
        self.unsC = tk.StringVar()
        self.unuA = tk.StringVar()
        self.unuB = tk.StringVar()
        self.unuC = tk.StringVar()
        self.sA.set(0)
        self.sB.set(0)
        self.sC.set(0)
        self.uA.set(0)
        self.uB.set(0)
        self.uC.set(0)
        self.unsA.set("")
        self.unsB.set("")
        self.unsC.set("")
        self.unuA.set("")
        self.unuB.set("")
        self.unuC.set("")
        self.checkbox_render()
        self.value_render()
        self.image_render()
        self.app.mainloop()

    def checkbox_render(self):
        """Stylování a vykreslování checkboxu."""
        # checkbox strany A
        self.chbsA = tk.Checkbutton(self.app, text=self.nazvy[1],
                                    variable=self.issA,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbsA.grid(row=0, column=0, sticky="W")
        # checkbox strany B
        self.chbsB = tk.Checkbutton(self.app, text=self.nazvy[2],
                                    variable=self.issB,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbsB.grid(row=0, column=1, sticky="W")
        # checkbox strany C
        self.chbsC = tk.Checkbutton(self.app, text=self.nazvy[3],
                                    variable=self.issC,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbsC.grid(row=0, column=2, sticky="W")
        # checkbox úhlu A
        self.chbuA = tk.Checkbutton(self.app, text=self.nazvy[4],
                                    variable=self.isuA,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbuA.grid(row=1, column=0, sticky="W")
        # checkbox úhlu B
        self.chbuB = tk.Checkbutton(self.app, text=self.nazvy[5],
                                    variable=self.isuB,
                                    command=self.count_of_true,
                                    fg="white", bg="#1d1d1d",
                                    activeforeground="white",
                                    activebackground="#1d1d1d",
                                    selectcolor="green", bd=5)
        self.chbuB.grid(row=1, column=1, sticky="W")
        # checkbox úhlu C
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
        self.right_panel_render()
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
        """Vypíná checkboxy po té co jsou vybrané 3."""
        if self.count >= 3:
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
        else:
            self.chbsA.configure(state="normal")
            self.chbsB.configure(state="normal")
            self.chbsC.configure(state="normal")
            self.chbuA.configure(state="normal")
            self.chbuB.configure(state="normal")
            self.chbuC.configure(state="normal")
    
    def image_render(self):
        trImg = tk.Canvas(self.app, bg="#1d1d1d", width=450, height=395, highlightbackground="#1d1d1d")
        trImg.grid(row=3, column=0, columnspan=3, sticky='we')
        trImg.create_text(35,360, anchor="w", text="A", fill="white",
                          font=("Helvetica","16", "bold"))
        trImg.create_text(405,360, anchor="w", text="B", fill="white",
                          font=("Helvetica","16", "bold"))
        trImg.create_text(225,25, anchor="center", text="C", fill="white",
                          font=("Helvetica","16", "bold"))
        trImg.create_text(225,360, anchor="center", text="strana c", 
                          fill="white", font=("Helvetica","12", "bold"))
        trImg.create_text(120,185, anchor="center", text="strana b",angle=60,
                          fill="white", font=("Helvetica","12", "bold"))
        trImg.create_text(330,185, anchor="center", text="strana a",angle=-60,
                          fill="white", font=("Helvetica","12", "bold"))
        trImg.create_text(105,310, anchor="center", text="\u03B1",
                          fill="white", font=("Helvetica","12", "bold"))
        trImg.create_text(345,310, anchor="center", text="\u03B2",
                          fill="white", font=("Helvetica","12", "bold"))
        trImg.create_text(225,105, anchor="center", text="\u03B3",
                          fill="white", font=("Helvetica","12", "bold"))
        uaA = trImg.create_arc(0,293.109,100,393.109, start=0, extent=60,
                               outline="white", width=1.5)
        uaB = trImg.create_arc(350,293.109,450,393.109, start=120,
                               extent=60, outline="white", width=1.5)
        uaC = trImg.create_arc(175,-10,275,90, start=240,
                               extent=60, outline="white", width=1.5)
        slC = trImg.create_line(50, 343.109, 400, 343.109, fill="white",
                                width=3)
        slA = trImg.create_line(400, 343.109, 225, 40, fill="white", width=3)
        slB = trImg.create_line(225, 40, 50, 343.109, fill="white", width=3)
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
        
        var = proměná pro uložení hodnoty.
        txt = nadpisek pro vkládání.
        values = 0 je délka, 1 jsou uhly
        myrow = radek
        mycolumn = pocatecni sloupec
        """
        
        tk.Label(self.frame, text=txt, bg="#1d1d1d", fg="white", bd=5,
                 anchor="n").grid(row=myrow, column=mycolumn, sticky="ne")
        tk.Spinbox(self.frame, bg="green", fg="white", from_=0.1,
                   to=10000, buttonbackground="#1d1d1d", increment=0.05,
                   width=10, textvariable=var).grid(row=myrow, sticky="we",
                                                    column=mycolumn+1)
        if values == 0:
            ol = ("mm", "cm","dm","m", "km")
            unit.set("m")
            self.om = tk.OptionMenu(self.frame, unit, *ol)
            self.om.config(bg="#1d1d1d", bd=5, fg="white", relief="flat",
                           highlightbackground="#1d1d1d", width=5,
                           activebackground="green", height=1,
                           activeforeground="white")
            self.om.grid(row=myrow, column=mycolumn+2, sticky="w")

        else:
            ol = ("\xb0", "rad","\u03c0 rad")
            unit.set("\xb0")
            self.om = tk.OptionMenu(self.frame, unit, *ol)
            self.om.config(bg="#1d1d1d", bd=5, fg="white", relief="flat",
                           highlightbackground="#1d1d1d", width=5,
                           activebackground="green", height=1,
                           activeforeground="white")
            self.om.grid(row=myrow, column=mycolumn+2, sticky="w")
        if self.count ==3:
            tk.Button(self.frame,text="Vypočítej", bg ="green", fg="white",
                      padx=185, pady=15, relief="flat",
                      activebackground="#7daa7d", activeforeground="white",
                      command=self.get_values, state="normal"
                      ).grid(row=3, column=3, columnspan=3, sticky="wn")
        else:
            tk.Button(self.frame,text="Vypočítej", bg ="#2d2d2d", fg="white",
                      padx=185, pady=15, relief="flat", state="disabled",
                      command=self.get_values
                      ).grid(row=3, column=3, columnspan=3, sticky="wn")
        
            
    def right_panel_render(self):
        self.frame = tk.Frame(self.app, width=450, bg="#1d1d1d")
        self.frame.grid(column=4, row=0, columnspan=6, rowspan = 5, sticky="wn")
        self.frame.grid_columnconfigure(3, minsize=250)
        self.frame.grid_columnconfigure(4, minsize=50)
        self.frame.grid_columnconfigure(5, minsize=50)
        if self.count > 0:
            self.app.minsize(900, 502)
            self.app.maxsize(900, 502)
        
            
            
    def blank(self, myrow, mycolumn):
        tk.Label(self.frame, width=55, bg="#1d1d1d", height=2
                 ).grid(row=myrow, column=mycolumn, columnspan=6, sticky="we")
    
    def input_render_choice(self):
        if self.issA.get():
            self.mysA = self.input_render(self.sA, "strana a", 0, 0, 3,
                                          self.unsA)
            if self.issB.get():
                self.input_render(self.sB, "strana b", 0, 1, 3, self.unsB)
                if self.issC.get():
                    self.input_render(self.sC, "strana c", 0, 2, 3, self.unsC)
                    self.submit_button()
                elif self.isuA.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuA)
                    self.submit_button()
                elif self.isuB.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuB)
                    self.submit_button()
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.issC.get():
                self.input_render(self.sC, "strana c", 0, 1, 3, self.unsC)
                if self.isuA.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuA)
                    self.submit_button()
                elif self.isuB.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuB)
                    self.submit_button()
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.isuA.get():
                self.input_render(self.uA, "úhel \u03B1", 1, 1, 3, self.unuA)
                if self.isuB.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuB)
                    self.submit_button()
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3, self.unuB)
                self.submit_button()
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.isuC.get():
                self.input_render(self.uC, "úhel \u03B3", 1, 1, 3, self.unuC)
                self.blank(2, 3)
                
            else:
                self.blank(1, 3)
                self.blank(2, 3)
                
        elif self.issB.get():
            self.input_render(self.sB, "strana b", 0, 0, 3, self.unsB)
            if self.issC.get():
                self.input_render(self.sC, "strana c", 0, 1, 3, self.unsC)
                if self.isuA.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuA)
                    self.submit_button()
                elif self.isuB.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuB)
                    self.submit_button()
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.isuA.get():
                self.input_render(self.uA, "úhel \u03B1", 1, 1, 3, self.unuA)
                if self.isuB.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuB)
                    self.submit_button()
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3, self.unuB)
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3,
                                      self.unuC)
                    self.submit_button()
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
                self.input_render(self.uA, "úhel \u03B1", 1, 1, 3, self.unuA)
                if self.isuB.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuB)
                    self.submit_button()
                elif self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3, self.unuB)
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
                else:
                    self.blank(2, 3)
                    
            elif self.isuC.get():
                self.input_render(self.uC, "úhel \u03B3", 1, 1, 3, self.unuC)
                self.blank(2, 3)
                
            else:
                self.blank(1, 3)
                self.blank(2, 3)
                
        elif self.isuA.get():
            self.input_render(self.uA, "úhel \u03B1", 1, 0, 3, self.unuA)
            if self.isuB.get():
                self.input_render(self.uB, "úhel \u03B2", 1, 1, 3, self.unuB)
                if self.isuC.get():
                    self.input_render(self.uC, "úhel \u03B3", 1, 2, 3, self.unuC)
                    self.submit_button()
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
            

            
    def submit_button(self):
        tk.Button(self.frame,text="Vypočítej", bg ="green", fg="white",
                  padx=185, pady=15, relief="flat", activebackground="#7daa7d",
                  activeforeground="white", command=self.get_values
                  ).grid(row=3, column=3, columnspan=3, sticky="wn")
        
    def get_values(self):
        Uprava_jednotek(self.sA.get(), self.sB, self.sC, self.uA, self.uB, self.uC,
                        self.unsA, self.unsB, self.unsC, self.unuA, self.unuB,
                        self.unuC)
        return sA
                
            

if __name__ == "__main__":
    Gui()