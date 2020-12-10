"""Cetnost znaku."""

from os import path
import collections

soubor = input("""Zadejte název dokumentu.\n
               Pokud soubor neexistuje, vytvoří se nový:\n""")
soubor = "ahoj.txt"


def fileExists(soubor):
    """Work With File."""
    if(path.exists(soubor)):
        x = open(soubor, "r")
        print(x.read())
    else:
        x = open(soubor, "w")
        x.write(input("Napište text, který chcete mít v novém souboru:\n\n"))
        x.close()
    return x


fileExists(soubor)


def textIntoVar(soubor):
    """Insert Text Into Variable."""
    with open(soubor, "r") as file:
        text = file.read().replace("\n", "")
    return text


# var with text
var = textIntoVar(soubor)


def charNum(var):
    """Num Of Characters."""
    celkem = 0
    for i in var:
        celkem += 1
    return celkem


def mostFreq(var):
    """Look For Most Used Character."""
    most = collections.Counter(var.lower()).most_common(1)[0]
    return most


def leastFreq(var):
    """Look For Least Used Characters."""
    all_freq = {}
    for i in var.lower():
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    least = min(all_freq, key=all_freq.get)
    return least


def numOfEachChar(var):
    """Num Of Each Characters In Text."""
    eachChar = {}
    for i in var.lower():
        if i in eachChar:
            eachChar[i] += 1
        else:
            eachChar[i] = 1
    return eachChar


# var of numEachChar
each = numOfEachChar(var)


def average(each):
    """Average."""
    pocetElements = len(each)
    return pocetElements


prumer = charNum(var)/average(each)


# method calling
charNum(var)
mostFreq(var)
leastFreq(var)
numOfEachChar(var)
average(each)


print(".............................................")
print("Počet znaků je ", charNum(var))
print("Nejpoužívanější znak je ", mostFreq(var))
print("Nejménně použitý znak je ", leastFreq(var))
print("Počet každého obsaženého znaku v textu je ")
print(numOfEachChar(var))
print("Pruměrná četnost je ", round(prumer, 2))


input("\nKlávesou ENTER ukončíte program...")
