def minimax(cislo):
    """
    Funkcia pre najdenie maxima a minima zadanej sekvencie cisiel.

    Funkcia vracia 4 hodnoty: minimum, index minium, maximum, index maximum (v poradi)
    >>> minimax([1, 2, 3, -1])
    (-1, 3, 3, 2)

    Implementacia hladania minima a maxima nevyuziva built-in funkcie
    min(x)/max(x), pretoze to pravdepodobne nebolo cielom tohoto zadania.
    Bezne by sme ale chceli vyuzit tieto funkcie, namiesto implementovania
    niecoho co jazyk samotny uz podporuje.
    """
    minimum = cislo[0]
    maximum = cislo[0]
    i_min = 0
    i_max = 0

    for i, cislo in enumerate(cislo):
        if cislo < minimum:
            minimum = cislo
            i_min = i 
        if cislo > maximum:
            maximum = cislo
            i_max = i 

    return minimum, i_min, maximum, i_max

def bubble_sort(cisla):
    cisla = cisla.copy()
    for i in range(1, len(cisla)):
        for j in range(len(cisla) -1):
            if cisla[j] > cisla[j+1]:
                cisla[j], cisla[j+1] = cisla [j+1], cisla[j]
    return cisla

cisla = [2,7,1,23,6]
zoradene = bubble_sort(cisla)
print(minimax(cisla))
print(zoradene)