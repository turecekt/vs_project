"""Soubor s tridicimi algoritmy."""


def bubblesort(pole):
    """Tridici algoritmus bubblesort."""
    for _ in pole:
        for j in range(len(pole) - 1):
            if pole[j] > pole[j + 1]:
                temp = pole[j]
                pole[j] = pole[j + 1]
                pole[j + 1] = temp

    print("Serazene pole:", pole)


def insertionsort(pole):
    """Tridici algoritmus insertionsort."""
    for i in range(1, len(pole)):
        prvek = pole[i]
        j = i - 1

        while j >= 0 and pole[j] > prvek:
            pole[j + 1] = pole[j]
            j -= 1

        pole[j + 1] = prvek

    print("Serazene pole:", pole)


def selectionsort(pole):
    """Tridici algoritmus selectionsort."""
    for i in range(len(pole)):
        minIndex = i
        for j in range(i + 1, len(pole)):
            if pole[j] < pole[minIndex]:
                minIndex = j
        pole[i], pole[minIndex] = pole[minIndex], pole[i]

    print("Serazene pole:", pole)
