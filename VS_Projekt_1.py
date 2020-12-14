""".

SEMESTRALNY PROJEKT NA AP1VS

VS_Projekt.py

version:    1.0

Author: Marek Mitrik      (https://github.com/Grontax)
        Jozef Varhanik    (https://github.com/jvarhanik)
        Michal Vojdan     (https://github.com/Migelvojto)

---------------------------------------------------

Tento algoritmus slúži na posúdenie či je zadané císlo prvočíslom

---------------------------------------------------

Projekt bol vytvorený pre vzdelávacie účely.

"""
cislo = int(input('Zadajte ľubovoľné prirodzené číslo: '))

# Hlavná funkcia
def prvocisla(a):
    """Definovanie funkcie."""
    global text
    global text2
    global PocetDelitelov
    PocetDelitelov = 0
    text = ''
    text2 = ''
    if cislo == 0:
        pass
    elif cislo % cislo == 0:
        PocetDelitelov += 1
    for i in range(1, 10):
        if cislo == i:
            PocetDelitelov += 0
        elif cislo % i == 0:
            PocetDelitelov += 1
        else:
            pass
    if cislo < 0:
        text = 'Zadané číslo nie je prirodzené číslo.'
        print(text)
    elif PocetDelitelov == 2:
        text = 'Číslo ' + str(cislo) + ' je prvočíslo.'
        print(text)
        if cislo < 10:
            text2 = 'Výsledok sme zistili pomocou metódy priameho delenia v cykle.'
            print(text2)
        elif cislo >= 10:
            text2 = 'Výsledok sme zistili pomocou štatistickej metódy.'
            print(text2)

    elif PocetDelitelov != 2:
        text = ('Číslo ' + str(cislo) + ' nie je prvočíslo.')
        print(text)
        if cislo < 10:
            text2 = 'Výsledok sme zistili pomocou metódy priameho delenia v cykle.'
            print(text2)
        elif cislo >= 10:
            text2 = 'Výsledok sme zistili pomocou štatistickej metódy.'
            print(text2)

# Unit testy
def test_prvocisla_delitelia():
    """Definicia funkcie na Unit Testy."""
    if cislo == 1:
        assert PocetDelitelov != 2

    if cislo == 2:
        assert PocetDelitelov == 2

    if cislo == 3:
        assert PocetDelitelov == 2

    if cislo == 4:
        assert PocetDelitelov != 2

    if cislo == 5:
        assert PocetDelitelov == 2

    if cislo == 6:
        assert PocetDelitelov != 2

    if cislo == 7:
        assert PocetDelitelov == 2

    if cislo == 8:
        assert PocetDelitelov != 2

    if cislo == 9:
        assert PocetDelitelov != 2

    if cislo == 10:
        assert PocetDelitelov != 2

    if cislo == 11:
        assert PocetDelitelov == 2

    if cislo == 12:
        assert PocetDelitelov != 2

    if cislo == 13:
        assert PocetDelitelov == 2

    if cislo == 14:
        assert PocetDelitelov != 2

    if cislo == 15:
        assert PocetDelitelov != 2

    if cislo == 16:
        assert PocetDelitelov != 2

    if cislo == 17:
        assert PocetDelitelov == 2

    if cislo == 18:
        assert PocetDelitelov != 2

    if cislo == 19:
        assert PocetDelitelov == 2

    if cislo == 20:
        assert PocetDelitelov != 2


prvocisla(cislo)
test_prvocisla_delitelia()
