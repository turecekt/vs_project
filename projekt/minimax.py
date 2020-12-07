"""Program pro nalezeni min a max z pole a nasledne serazeni pole."""
import sys
from os import path
import random


# Funkce pro nalezení největšího a nejmenšího čísla a jejich indexů
def minmax(_list):
    """Najde min a max z pole + jejich indexy."""
    if(len(_list) > 0):
        max = _list[0]
        indexMax = 0
        min = _list[0]
        indexMin = 0
        for index, item in enumerate(_list):
            if item > max:
                max = item
                indexMax = index
            if item < min:
                min = item
                indexMin = index
        return str(max), str(min), str(indexMax), str(indexMin)
    else:
        return "0", "0", "0", "0"


# Implementace bubblesortu
def bubblesort(_list):
    """Bubblesort funkce."""
    for x in range(len(_list)-1):
        for k in range(len(_list) - x - 1):
            if _list[k+1] < _list[k]:
                pomocne = _list[k+1]
                _list[k+1] = _list[k]
                _list[k] = pomocne


# Implementace insertion sortu
def insertion_sort(_list):
    """Insertionsort funkce."""
    for x in range(1, len(_list)):
        j = x-1
        dalsiCislo = _list[x]

        while (_list[j] > dalsiCislo) and (j >= 0):
            _list[j+1] = _list[j]
            j = j-1
        _list[j+1] = dalsiCislo


# Implementace selection sortu
def selection_sort(_list):
    """Selectionsort funkce."""
    for x in range(len(_list)):
        minIndex = x
        for j in range(x + 1, len(_list)):
            if _list[minIndex] > _list[j]:
                minIndex = j

        _list[x], _list[minIndex] = _list[minIndex], _list[x]


def testMinMax():
    """Pytest test."""
    poleProTest = [1, 2, 3]
    assert minmax(poleProTest) == ("3", "1", "2", "0")


# Řešení pro vstupní paramatery:
pole = []
obsahujeChybu = False
if len(sys.argv) > 1:
    sys.argv.pop(0)
    if(path.exists(sys.argv[0])):
        file = open(sys.argv[0], encoding='utf8')
        words = file.read().splitlines()
        file.close()
        data = []
        for x in words:
            data = x.split()
            for k in data:
                try:
                    TryParse = int(k)
                    pole.append(TryParse)
                except ValueError:
                    obsahujeChybu = True
    else:
        for x in sys.argv:
            try:
                TryParse = int(x)
                pole.append(TryParse)
            except ValueError:
                obsahujeChybu = True
else:
    pole = [random.randint(1, 100) for _ in range(10)]

# Zavolání funkce
vysledek = minmax(pole)

print("Největší číslo: " + vysledek[0] + " a jeho index: " + vysledek[2])
print("Největší číslo: " + vysledek[1] + " a jeho index: " + vysledek[3])

# Volba řadících funkcí uživatelem
a = input("Zvolte, jakou řadící funkcí chcete vaše pole seřadit: \
    (1 = Bubblesort, 2 = Insertion sort, 3 = Selection sort)\n")

# "Switch" pro volbu uživatele
if a == "1":
    bubblesort(pole)
elif a == "2":
    insertion_sort(pole)
elif a == "3":
    selection_sort(pole)
else:
    print("Nezadali jste správnou volbu!")

# Vypsání pole, vypíše se i při nesprávném zadání řadícího algoritmu
print(pole)
