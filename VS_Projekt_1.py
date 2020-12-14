""".

SEMESTRALNY PROJEKT NA AP1VS

VS_Projekt.py



Autori: Marek Mitrik      (https://github.com/Grontax)
        Jozef Varhanik    (https://github.com/jvarhanik)
        Michal Vojdan     (https://github.com/Migelvojto)

---------------------------------------------------

Tento algoritmus slúži na posúdenie či je zadané císlo prvočíslom

---------------------------------------------------

Projekt bol vytvorený pre vzdelávacie účely.

"""
global cislo
cislo = int(input('Zadajte ľubovoľné prirodzené číslo: '))


# Hlavná funkcia
def prvocisla(a):
    """Definovanie hlavnej funkcie na vyhodnotenie prvočísel."""
    global text
    global text2  # Definovanie globálnych premenných.
    global PocetDelitelov
    PocetDelitelov = 0
    text = ''
    text2 = ''
    if cislo == 0:
        pass
    elif cislo % cislo == 0:
        PocetDelitelov += 1  # Podmienky na určenie počtu deliteľov.
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
        print(text)  # Podmienky na určenie výstupného textu prvočísla.
        if cislo < 10:
            text2 = 'Metóda priameho delenia v cykle.'
            print(text2)
        elif cislo >= 10:
            text2 = 'Výsledok sme zistili pomocou štatistickej metódy.'
            print(text2)

    elif PocetDelitelov != 2:
        text = ('Číslo ' + str(cislo) + ' nie je prvočíslo.')
        print(text)  # Podmienky na určenie výstupného textu neprvočísel.
        if cislo < 10:
            text2 = 'Metóda priameho delenia v cykle.'
            print(text2)
        elif cislo >= 10:
            text2 = 'Výsledok sme zistili pomocou štatistickej metódy.'
            print(text2)


# Unit testy
def test_prvocisla_delitelia():
    """Testovacia funkcia na prvých 20 prirodzených čísel."""
    if cislo == 1:
        assert PocetDelitelov != 2

    elif cislo == 2:
        assert PocetDelitelov == 2

    elif cislo == 3:
        assert PocetDelitelov == 2

    elif cislo == 4:
        assert PocetDelitelov != 2

    elif cislo == 5:
        assert PocetDelitelov == 2

    elif cislo == 6:
        assert PocetDelitelov != 2

    elif cislo == 7:
        assert PocetDelitelov == 2

    elif cislo == 8:
        assert PocetDelitelov != 2

    elif cislo == 9:
        assert PocetDelitelov != 2

    elif cislo == 10:
        assert PocetDelitelov != 2  # Otestuje prvých 20 čísel.

    elif cislo == 11:
        assert PocetDelitelov == 2

    elif cislo == 12:
        assert PocetDelitelov != 2

    elif cislo == 13:
        assert PocetDelitelov == 2

    elif cislo == 14:
        assert PocetDelitelov != 2

    elif cislo == 15:
        assert PocetDelitelov != 2

    elif cislo == 16:
        assert PocetDelitelov != 2

    elif cislo == 17:
        assert PocetDelitelov == 2

    elif cislo == 18:
        assert PocetDelitelov != 2

    elif cislo == 19:
        assert PocetDelitelov == 2

    elif cislo == 20:
        assert PocetDelitelov != 2


def test_parnecisla():
    """Testovacia funkcia na párne čísla."""
    for n in range(4, 100000000, 2):
        if cislo == n:
            assert PocetDelitelov != 2


def test_prvocislamale():
    """Testovacia funkcia na prvočísla v prvej stovke."""
    pole = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]  # Zoznam.
    for i in range(0, len(pole) - 1):  # Pomocou cyklu zistíme index poľa.
        if cislo == pole[i]:
            assert PocetDelitelov == 2


def test_prvocislavelke():
    """Testovacia funkcia na prvočísla nad 1000."""
    pole = [1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]  # Zoznam.
    for i in range(0, len(pole) - 1):  # Pomocou cyklu zistíme index poľa.
        if cislo == pole[i]:
            assert PocetDelitelov == 2


prvocisla(cislo)
test_prvocisla_delitelia()
test_parnecisla()
test_prvocislavelke()
test_prvocislamale()
