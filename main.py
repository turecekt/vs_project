import sys

from os.path import exists
from collections import Counter


line = "-" * 45 # separator
occurrence = {}
num = 0
alpha = 0
other_sym = 0
text = ""

# spouštění programu: "py main.py"
# spouštění programu s textovým souborem: "py main.py soubor.txt"

def main():


    if sys.argv[1:]:
        if sys.argv[1].endswith(".txt") or sys.argv[1].endswith(".log"):
            if exists(sys.argv[1]):
                file = open(sys.argv[1], "r+")
                text = file.read()
                file.close()
            else:
                print("\nSoubor nenalezen.")
                exit()
        else:
            print("\nByl zadán špatný formát souboru.")
            exit()
    else:
        while True:
            input_text = input("Zadejte textový řetězec: ")
            if '#' in input_text:
                text = text + input_text.split('#', 1)[0]
                break
            text = text + input_text

    if len(text) == 0:
        print("\n Nebyl zadán žádný text.")
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

    # TODO Zaokrouhlení
    print("\nPrůměrná četnost")
    rounded_average = round(len(text) / len(sorted(Counter(text))), 2)
    print(rounded_average)

    print(line)

    count_to_dictionary(text)
    char_type_counting(alpha, num, other_sym)
    occurrence_graph()


# TODO Bonus - počet čísel, počet písmen, počet speciálních znaků

def char_type_counting(alpha, num, other_sym):

    for key, value in occurrence.items():
        if key.isalpha():
            alpha += 1
        elif key.isdigit():
            num += 1
        else:
            other_sym += 1

    print("Počet písmen")
    print(alpha)

    print("Počet čísel")
    print(num)

    print("Počet specialních symbolů")
    print(other_sym)

def count_to_dictionary(text):
    for char in text:
        if char != "\n":
            if char in occurrence:
                occurrence[char] = occurrence[char] + 1
            else:
                occurrence[char] = 1


# Graf četnost znaků
def occurrence_graph():

    max_value = 0

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