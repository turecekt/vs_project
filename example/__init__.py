def minimax(cislo):
    """
    Funkcia pre najdenie maxima a minima zadanej sekvencie cisiel.

    Funkcia vracia 2 hodnoty: minimum, maximum (v poradi)
    >>> minimax([1, 2, 3, -1])
    (-1, 3)

    Implementacia hladania minima a maxima nevyuziva built-in funkcie
    min(x)/max(x), pretoze to pravdepodobne nebolo cielom tohoto zadania.
    Bezne by sme ale chceli vyuzit tieto funkcie, namiesto implementovania
    niecoho co jazyk samotny uz podporuje.
    """
    minimum = cislo[0]
    maximum = cislo[0]

    for num in cislo:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


print(minimax([1, 2, 3, -1]))
