"""Cetnost znaku."""

from os import path
import collections

print("Zadejte název dokumentu:")
soubor = input("Pokud soubor neexistuje, vytvoří se nový: \n")


def fileExists():
    """Work With File."""
    if(path.exists(soubor)):
        x = open(soubor, "r")
        print(x.read())
    else:
        x = open(soubor, "w")
        x.write(input("Napište text, který chcete mít v novém souboru:\n\n"))
        x.close()


fileExists()


def textIntoVar():
    """Insert Text Into Variable."""
    with open(soubor, "r") as file:
        text = file.read().replace("\n", "")
    return text


# var with text
var = textIntoVar()


def charNum():
    """Num Of Characters."""
    celkem = 0
    for i in var:
        celkem += 1
    return celkem


def mostFreq():
    """Look For Most Used Character."""
    most = collections.Counter(var.lower()).most_common(1)[0]
    return most


def leastFreq():
    """Look For Least Used Characters."""
    all_freq = {}
    for i in var.lower():
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    least = min(all_freq, key=all_freq.get)
    return least


def numOfEachChar():
    """Num Of Each Characters In Text."""
    eachChar = {}
    for i in var.lower():
        if i in eachChar:
            eachChar[i] += 1
        else:
            eachChar[i] = 1
    return eachChar


# var of numEachChar
each = numOfEachChar()


def average():
    """Average."""
    pocetElements = len(each)
    return pocetElements


prumer = charNum()/average()


# method calling
charNum()
mostFreq()
leastFreq()
numOfEachChar()
average()


print(".............................................")
print("Počet znaků je ", charNum())
print("Nejpoužívanější znak je ", mostFreq())
print("Nejménně použitý znak je ", leastFreq())
print("Počet každého obsaženého znaku v textu je ")
print(numOfEachChar())
print("Pruměrná četnost je ", round(prumer, 2))


input("\nKlávesou ENTER ukončíte program...")
