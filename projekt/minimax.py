import sys
import os.path
from os import path
import random

def minmax():
    max = pole[0]
    indexMax = 0
    min = pole[0]
    indexMin = 0
    for index, item in enumerate(pole):
        if item > max:
            max = item
            indexMax = index
        if item < min:
            min = item
            indexMin = index
    print("Největší číslo: " + str(max) + " a jeho index: " + str(indexMax))
    print("Největší číslo: " + str(min) + " a jeho index: " + str(indexMin))

def bubblesort(list):

    for x in range(len(pole)-1):
        for k in range(len(pole) - x - 1):
            if pole[k+1] < pole[k]:
                pomocne = pole[k+1]
                pole[k+1] = pole[k]
                pole[k] = pomocne


pole = []
if len(sys.argv) > 1:
    sys.argv.pop(0)
    if(path.exists(sys.argv[0])):
        file = open(sys.argv[0], "r")
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
                    sys.exit("Všechny vstupy musí být typu int!")
    else:
        for x in sys.argv:
            try:
                TryParse = int(x)
                pole.append(TryParse)
            except ValueError:
                sys.exit("Všechny vstupy musí být typu int!")
else:
    pole = [random.randint(1,100) for _ in range(10)]

minmax()
bubblesort(pole)
print(pole)



