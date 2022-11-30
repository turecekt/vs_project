import sys
import collections

from collections import Counter


line = "-" * 45 # separator


# spouštění programu: "py main.py"
# spouštění programu s textovým souborem: "py main.py soubor.txt"

def main():
    text = ""
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
                text = text + input_text.split('#', 1)[0]
                break
            text = text + input_text

    # TODO prázdný text ukončí program, nějak vylepšit
    if len(text) == 0:
        exit()


    # TODO Vytvořit metody a v main() je jen volat
    # TODO Přehlednější výpisy např.: "Celkový počet znaků: 123"
    print("Celkový počet znaků")
    print(len(text))

    # TODO "abeceda" 2x "a" 2x "e" - ale musí vypsat oboje
    print("\nNejčastější znak")
    print(Counter(text).most_common(1))

    print("\nNejméně častý znak")
    print(Counter(text).most_common()[-1])

    print("\nPrůměrná četnost")
    print(len(text) / len(sorted(Counter(text))))

    print(line)

    occurrence_graph(text)


# TODO Bonus - počet čísel, počet písmen, počet speciálních znaků


# Graf četnost znaků
def occurrence_graph(text):
    occurrence = {}
    max_value = 0

    for char in text:
        if char in occurrence:
            occurrence[char] = occurrence[char] + 1
        else:
            occurrence[char] = 1

    for key, value in occurrence.items():
        if value > max_value:
            max_value = value

    if max_value <= len("OCCURRENCES"):
        print(f"CHAR|OCCURRENCES|NR.")
    else:
        print(f"CHAR|OCCURRENCES{' ' * (max_value - len('OCCURRENCES'))}|NR.")
    print(line)

    for key, value in sorted(occurrence.items()):
        if max_value > len("OCCURRENCES"):
            print(f"   {key}|{'*' * value}{' ' * (max_value-value)}|{value}")
        else:
            print(f"   {key}|{'*' * value}{' ' * (len('OCCURRENCES')-value)}|{value}")

    print(line)

if __name__ == "__main__":
    main()