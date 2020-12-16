""".

SEMESTRALNY PROJEKT DO AP1VS

VS_Projekt.py

version:    1.1

Author: Marek Mitrik      (https://github.com/Grontax)
        Jozef Varhanik    (https://github.com/jvarhanik)
        Michal Vojdan     (https://github.com/Migelvojto)

---------------------------------------------------

This algorithm is used to define if a
value entered by the user is a prime number

---------------------------------------------------

This project was made for educational purpose only.

"""


def vypocti_delitelov(cislo):
    """Funkcia na hladanie poctu delitelov daneho cisla."""
    pocet_delitelov = 0
    if cislo > 10:
        pocet_delitelov = 1
    for i in range(1, 10):
        if cislo % i == 0:
            pocet_delitelov = pocet_delitelov + 1
    return pocet_delitelov  # Vratenie poctu delitelov


def je_prvocislo(cislo):
    """Funkcia na vyhodnotenie ci je cislo prvocislo alebo nie."""
    pocet_delitelov = vypocti_delitelov(cislo)
    if cislo < 0:
        return None  # Vratenie hodnoty none
    elif pocet_delitelov == 2:
        return True  # Vratenie hodnoty true
    elif pocet_delitelov != 2:
        return False  # Vratenie hodnoty false


def popis(cislo):
    """Funkcia na urcenie popisu podla podmienok."""
    text = ' '
    text2 = ' '
    prvocislo = je_prvocislo(cislo)
    if prvocislo is None:
        text = 'Zadané číslo nie je prirodzené číslo.'
    elif prvocislo is False:
        text = ('Číslo ' + str(cislo) + ' nie je prvočíslo')
    elif prvocislo is True:
        text = ('Číslo ' + str(cislo) + ' je prvočíslo')
# Podmienky ktore nam zmenia hodnotu textu
    if cislo < 0:
        text2 = ''
    elif cislo >= 10:
        text2 = 'Štatistická metóda'
    elif cislo < 10:
        text2 = 'Priame delenie v cykle.'
# podmienky ktore menia hodnotu textu 2
    return [text, text2]


def test_vypocti_delitelov():
    """Unit test na kontrolu poctu delitelov."""
    assert vypocti_delitelov(19) == 2
    assert vypocti_delitelov(20) != 2
# Unit test otestuje vstup 19 a 20


def test_je_prvocislo():
    """Unit test na skontrolovanie spravnosti urcenia BOOL hodnoty."""
    assert je_prvocislo(-1) is None
    assert je_prvocislo(3) is True
    assert je_prvocislo(4) is False
# Unit test otestuje ci zadane cislo je prvocislo


def test_popis():
    """Unit test na kontrolu zadanych popisov."""
    assert popis(-1) == ['Zadané číslo nie je prirodzené číslo.', '']
    assert popis(3) == ['Číslo 3 je prvočíslo', 'Priame delenie v cykle.']
    assert popis(12) == ['Číslo 12 nie je prvočíslo', 'Štatistická metóda']
# Vkladanie textu


if __name__ == '__main__':
    print(popis(int(input('Zadajte ľubovoľné prirodzené číslo: '))))
