import sys
import collections

from collections import Counter

text = ""

# spouštění programu: "py main.py"
# spouštění programu s textovým souborem: "py main.py soubor.txt"


# TODO Error, když soubor neexistuje
# TODO Soubor musí být jen .txt
if (sys.argv[1:]):
    file = open(sys.argv[1], "r+")
    text = file.read()
    file.close()
else:
    while True:
        input_text = input("Zadejte textový řetězec: ")
        if '#' in input_text:
            text = text + input_text.split('#',1)[0]
            break
        text = text + input_text    



# TODO Přehlednější výpisy např.: "Celkový počet znaků: 123"
print("Celkový počet znaků")
print(len(text))

# TODO "abeceda" 2x "a" 2x "e" - ale musí vypsat oboje
print("\nNejčastější znak")
print(Counter(text).most_common(1))

print("\nNejméně častý znak")
print(Counter(text).most_common()[-1])

print("\nPrůměrná četnost")
print(len(text)/len(sorted(Counter(text))))

print("\nČetnost jednotlivých znaků")
print(Counter(text))

# TODO Bonus - počet čísel, počet písmen, počet speciálních znaků

# TODO Bonus graf - Dominik
"""
---------------------------------------------
LEN|OCCURRENCES |NR.
---------------------------------------------
  1|*           |1
  2|*********   |9
  3|******      |6
  4|*********** |11
  5|************|12
  6|***         |3
  7|****        |4
  8|*****       |5
  9|*           |1
 10|*           |1
 11|*           |1
"""