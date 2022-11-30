import sys
import collections

from collections import Counter

text = ""

if (sys.argv[1:]):
    file = open(sys.argv[1], "r+")
    text = file.read()
    file.close()
else:
    while True:
        input_text = input("Zadejte textový řetězec:")
        if '#' in input_text:
            text = text + input_text.split('#',1)[0]
            break
        text = text + input_text    

print("Celkový počet znaků")
print(len(text))

print("\nNejčastější znak")
print(Counter(text).most_common(1))

print("\nNejméně častý znak")
print(Counter(text).most_common()[-1])

print("\nPrůměrná četnost")
print(len(text)/len(sorted(Counter(text))))

print("\nČetnost jednotlivých znaků")
print(Counter(text))