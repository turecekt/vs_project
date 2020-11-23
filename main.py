import sys
import random

cisla = []
platnyVStup = True

# zadny vstupni argument - nahodna cisla
if len(sys.argv) == 1:
    cisla = [random.randint(0, 100) for i in range(20)]

# vstupni argument nazev souboru
elif len(sys.argv) == 2:
    nazevSouboru = sys.argv[1]
    soubor = open(nazevSouboru, "r")
    obsah = soubor.read()
    cislaString = obsah.split(" ")

    try:
        cisla = list(map(int, cislaString))
    except ValueError:
        platnyVStup = False
        print(
            "Nespravny format souboru - musi obsahovat pouze cela cisla oddelena mezerou.")

    soubor.close()

# vstupni argumenty cisla
else:
    for i in range(1, len(sys.argv)):
        try:
            cisla.append(int(sys.argv[i]))
        except ValueError:
            platnyVStup = False
            print("Vstupni argumenty musi byt cela cisla!")
            break

if platnyVStup:
    print(cisla)
