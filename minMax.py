def minMax(pole):

    min = pole[0]
    minIndex = 0
    max = pole[0]
    maxIndex = 0

    for i in range(1, len(pole)):

        if pole[i] < min:
            min = pole[i]
            minIndex = i

        if pole[i] > max:
            max = pole[i]
            maxIndex = i

    print("Minimum je cislo", min, "na indexu", minIndex)
    print("Maximum je cislo", max, "na indexu", maxIndex)


pole = [3, 2, 5, 5, 4, 3, 8]
print(pole)
minMax(pole)
