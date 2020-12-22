"""Finální verze.

Janák, Mikeska, Peterek, Novotný
"""


from tkinter import Label, Button, Entry, Tk, StringVar


def test_checkcorrect1():
    """Funkce pro kontrolu z num na rim.

    Testovaci funkce kontrolu
    >>> makeguifordecode("15")
    'XV'
    >>> makeguifordecode("1589")
    'MDLXXXIX'
    >>> makeguifordecode("347")
    'CCCVLII'
    >>> makeguifordecode("9")
    'IX'
    """


def test_checkcorrect():
    """Funkce pro kontrolu z rim na num.

    Testovaci funkce kontrolu
    >>> makeguiforencode("LL")
    False
    >>> makeguiforencode("IMI")
    False
    >>> makeguiforencode("ILM")
    False
    >>> makeguiforencode("CCCCC")
    False
    >>> makeguiforencode("LLL")
    False
    >>> makeguiforencode("LC")
    False
    >>> makeguiforencode("AA")
    False
    >>> makeguiforencode("IM")
    999
    >>> makeguiforencode("I")
    1
    >>> makeguiforencode("III")
    3
    """


def makeoptionmenu():
    """Gui na vyber menu.

    Pak spusti urcitou funkci
    """
    hlavni = Tk()
    hlavni.option_add('*Font', 'Arial 9')
    hlavni.title("Vyber")
    hlavni.resizable(False, False)

    def dec():
        hlavni.destroy()
        makeguifordecode("")

    def enc():
        hlavni.destroy()
        makeguiforencode("")

    btndec = Button(hlavni, text="Z numerického čísla na římská", command=dec)
    btnen = Button(hlavni, text="Z římského čísla na numerická", command=enc)
    btndec.grid(row=0, column=0, pady=10, padx=10)
    btnen.grid(row=1, column=0, pady=10)
    hlavni.mainloop()
    return


def makeguifordecode(x):
    """Obsahu GUI.

    Plus funkce pro zakodovani do rim
    """
    def menu():
        gui.destroy()
        makeoptionmenu()

    def decode(numb, cislo):
        """Funkce pro prevod z numerickeho cisla na rimska cisla 1. cast.

        Vstup číslo plus v jakem řádu, vystup je řetězec decodovaný
        """
        cisla = ["I", "V", "X", "X", "L", "C", "C", "D", "M"]
        p = ""
        if(numb <= 3):
            p += numb*cisla[(cislo*3-3)]
        elif(numb == 4):
            p += cisla[(cislo*3-3)]+cisla[1+(cislo*3-3)]
        elif(numb >= 5 and numb <= 8):
            p += cisla[1+(cislo*3-3)]+numb % 5*cisla[(cislo*3-3)]
        else:
            p += cisla[cislo*3-3]+cisla[2+(cislo*3-3)]
        return p

    def decodetorim(cislo):
        """Hlavni funkc.

        Vstup číslo které se bude převádět, vystup ve formátu pole bez tisíců
        """
        pokracuj = False
        textinrome = ""
        try:
            int(cislo)
            pokracuj = True
            if x == "":
                info.set(cislo + " je v římských:")
        except ValueError:
            if x == "":
                natextrome.set("Zadávej celé čísla. Jinak nebudu funkovat.")
                info.set("")
        if(pokracuj):
            number = cislo
            listofrome = []
            num = 0
            size = len(number)
            if(size >= 4):
                textinrome += int((number[0:size-3]))*"M"
                num = number[-3:]
            else:
                num = number
            d = 1
            while d <= 3 and d <= size:
                a = decode(int(num[-d]), d)
                d = d+1
                listofrome.append(a)
            pocitadlo = 0
            while pocitadlo+1 < size and pocitadlo+1 < 3:
                z = listofrome[pocitadlo] != ""
                if z and listofrome[pocitadlo+1] != "":
                    q, y = finalupdate(pocitadlo, pocitadlo+1, listofrome)
                    listofrome[pocitadlo] = q
                    listofrome[pocitadlo+1] = y
                pocitadlo = pocitadlo+1
            listofrome.reverse()
            for r in listofrome:
                textinrome += r
            if x == "":
                natextrome.set(textinrome)
        return textinrome

    def finalupdate(firstint, secondint, listofrome):
        """Funkce pro minimalizaci rimska cisla z 1. cast.

        Vstup 2x číslo které je z předchozí funkce, výstup je co zbylo
        """
        cisla = ["I", "V", "X", "L", "C", "D", "M"]
        x = ""
        y = ""
        pok1 = False
        pok2 = len(listofrome[secondint]) == 2
        if pok2:
            pok1 = listofrome[secondint][0] != listofrome[secondint][1]
        q = cisla.index(listofrome[firstint][0])
        pok3 = q - cisla.index(listofrome[secondint][0]) == -1
        pok4 = listofrome[firstint][-1] == listofrome[secondint][0]
        if pok4 and len(listofrome[firstint]) == 2 and pok2 and pok1:
            y += listofrome[firstint][0] + listofrome[secondint][1:]
        elif pok3 and pok2 and pok1:
            y += listofrome[firstint][0] + listofrome[secondint][1:]
            x += listofrome[firstint][1:]
        else:
            x += listofrome[firstint]
            y += listofrome[secondint]
        return x, y
    if x == "":
        gui = Tk()
        gui.option_add('*Font', 'Arial 9')
        gui.title("římská")
        gui.resizable(False, False)
        natextrome = StringVar()
        info = StringVar()
        textrim = Label(gui, text="Zadej numerické  číslo:")
        vstup = Entry(gui)
        btndec = Button(gui, fg="Blue", text="PŘEVEĎ",
                        command=lambda: decodetorim(vstup.get()))
        btnmenu = Button(gui, text="Zpět na menu", command=menu)
        textrimdecode = Label(gui, textvariable=info)
        btnen = Label(gui, textvariable=natextrome)
        textrim.grid(row=0, column=0, pady=10, padx=10)
        vstup.grid(row=0, column=1, pady=10, padx=10)
        btndec.grid(row=1, column=0, columnspan=2)
        textrimdecode.grid(row=2, column=0, columnspan=2)
        btnen.grid(row=3, column=0, columnspan=2)
        btnmenu.grid(row=4, column=0, columnspan=2)
        gui.mainloop()
    else:
        x = decodetorim(x)
    return x


def makeguiforencode(n):
    """Prevede rim cislo.

    Mikeska Janák
    """
    def menu():
        gui.destroy()
        makeoptionmenu()

    def checkcorrect(numb):
        """Funkce pro zjištění jestli je  ř. č. v dobrem tvaru).

        Vystup bool
        """
        dobre = True
        cisla = ["I", "V", "X", "L", "C", "D", "M"]
        coun = 0
        pocitadlostejnychznaku = 1
        maxy = "M"
        u = 0
        while u < len(numb):
            if numb[u] not in cisla:
                dobre = False
            u = u+1
        if dobre:
            if (len(numb) > 0):
                while coun+1 < len(numb):
                    x = cisla.index(numb[coun])
                    if (x % 2 == 1 and x + 1 == cisla.index(numb[coun + 1])):
                        dobre = False
                    if cisla.index(numb[coun]) < cisla.index(numb[coun+1]):
                        maxy = (numb[coun])
                        if coun+2 < len(numb):
                            q = cisla.index(numb[coun+1])
                            if q <= cisla.index(numb[coun+2]):
                                dobre = False
                    elif cisla.index(numb[coun]) > cisla.index(maxy):
                        dobre = False
                    else:
                        if numb[coun] != "M" and maxy == numb[coun]:
                            pocitadlostejnychznaku = pocitadlostejnychznaku+1
                            d = (maxy == "L" or maxy == "V" or maxy == "D")
                            if pocitadlostejnychznaku > 3:
                                dobre = False
                            elif pocitadlostejnychznaku > 1 and d:
                                dobre = False
                        else:
                            maxy = numb[coun]
                            pocitadlostejnychznaku = 1
                    coun = coun+1
                if numb[len(numb)-1] != "M" and maxy == numb[len(numb)-1]:
                    pocitadlostejnychznaku = pocitadlostejnychznaku+1
                    d = (maxy == "L" or maxy == "V" or maxy == "D")
                    if pocitadlostejnychznaku > 3:
                        dobre = False
                    elif pocitadlostejnychznaku > 1 and d:
                        dobre = False
        return dobre

    def suma(value):
        """Funkce pro prepocet.

        Vstup sting vystup int
        """
        cisla = ["I", "V", "X", "L", "C", "D", "M"]
        cislaar = [1, 5, 10, 50, 100, 500, 1000]
        x = 0
        if len(value) > 1:
            x = x-cislaar[cisla.index(value[0])]
            x = x+cislaar[cisla.index(value[1])]
        else:
            x = x+cislaar[cisla.index(value[0])]
        return x

    def encodefromrim(number):
        number = number.upper()
        cisl = ["I", "V", "X", "L", "C", "D", "M"]
        pokracuj2 = checkcorrect(number)
        if(pokracuj2):
            hodnota = 0
            position = 0
            while position < len(number):
                if position+1 < len(number):
                    x = cisl.index(number[position])
                    if x < cisl.index(number[position+1]):
                        p = number[position]+number[position+1]
                        hodnota = hodnota+suma(p)
                        position = 1+position
                    else:
                        hodnota = hodnota+suma(number[position])
                else:
                    hodnota = hodnota+suma(number[position])
                position = 1+position
            if n == "":
                natextrome.set(hodnota)
                info.set(number + " je v numerických:")
            return hodnota
        else:
            vypis = True
            u = 0
            while u < len(number):
                if number[u] not in cisl:
                    vypis = False
                u = u+1
            if vypis:
                if n == "":
                    natextrome.set("Máš chybu v syntaxi římského čísla.")
            else:
                if n == "":
                    natextrome.set("Zadávej jen římská čísla.")
            if n == "":
                info.set("")
            return pokracuj2
    if n == "":
        gui = Tk()
        gui.option_add('*Font', 'Arial 9')
        gui.title("římská číslice")
        natextrome = StringVar()
        info = StringVar()
        textrim = Label(gui, text="Zadej římské číslo:")
        vstup = Entry(gui)
        b = Button(gui, fg="Blue", text="PŘEVEĎ",
                   command=lambda: encodefromrim(vstup.get()))
        btnmenu = Button(gui, text="Zpět na menu", command=menu)
        textrimdecode = Label(gui, textvariable=info)
        btnen = Label(gui, textvariable=natextrome)
        textrim.grid(row=0, column=0, pady=10, padx=10)
        vstup.grid(row=0, column=1, pady=10, padx=10)
        b.grid(row=1, column=0, columnspan=2)
        textrimdecode.grid(row=2, column=0, columnspan=2)
        btnen.grid(row=3, column=0, columnspan=2)
        btnmenu.grid(row=4, column=0, columnspan=2)
        gui.mainloop()
    else:
        n = encodefromrim(n)
    return n


if __name__ == '__main__':
    makeoptionmenu()
