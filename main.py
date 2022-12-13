"""Missing docstring line."""
import sys

from os.path import exists

line_separator = "-" * 45
char_occurrence_dict = {}
alphabet_chars_dict = {}


def main():
    """Be the main function of this program.

    :return: None
    """
    text = ""

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

    char_counter = count_to_dictionary(text)
    min_values = char_min_values(char_occurrence_dict)
    max_values = char_max_values(char_occurrence_dict)
    rounded_average = char_average(char_occurrence_dict)
    occurrence_to_alphabetic_dict(char_occurrence_dict)

    # Celkový počet znaků
    print(f"Celkový počet znaků: {char_counter}")

    # Nejméně časté znaky
    if len(min_values) > 1:
        print(f"Nejméně časté znaky: {min_values}")
    else:
        print(f"Nejméně častý znak: '{min_values[0]}'")

    # Nejčastější znaky
    if len(max_values) > 1:
        print(f"Nejčastější znaky: {max_values}")
    else:
        print(f"Nejčastější znak: '{max_values[0]}'")

    # Průměrná četnost
    print(f"Průměrná četnost: {rounded_average}")

    if len(alphabet_chars_dict) > 0:
        # Výskyt znaků abecedy
        print("Četnost jednotlivých znaků abecedy:")

        # Výskyt znaků abecedy v grafu
        alphabet_occurrence_graph(alphabet_chars_dict)


def error_raiser(char_occurrence_dict):
    """Check the parameter's type.

    :param char_occurrence_dict: Dictionary with char occurrence.
    :return: None
    """
    if type(char_occurrence_dict) != dict:
        raise TypeError("Parametr musí být typu dictionary.")


def char_average(char_occurrence_dict):
    """Count an average quantity of chars, rounded with 2 decimals.

    :param char_occurrence_dict: Dictionary with char occurrence.
    :return: rounded_average
    """
    error_raiser(char_occurrence_dict)

    rounded_average = \
        round(sum(char_occurrence_dict.values())/len(char_occurrence_dict), 2)
    return rounded_average


def char_min_values(char_occurrence_dict):
    """Count the least frequent character.

    :param char_occurrence_dict: Dictionary with char occurrence.
    :return: min_values
    """
    error_raiser(char_occurrence_dict)

    min_values = \
        [key for key, value in char_occurrence_dict.items()
         if value == min(char_occurrence_dict.values())]
    return min_values


def char_max_values(char_occurrence_dict):
    """Count the most frequent character.

    :param char_occurrence_dict: Dictionary with char occurrence.
    :return: max_values
    """
    error_raiser(char_occurrence_dict)

    max_values = \
        [key for key, value in char_occurrence_dict.items()
         if value == max(char_occurrence_dict.values())]
    return max_values


def occurrence_to_alphabetic_dict(char_occurrence_dict):
    """Save only letters from char_occurrence_dict to alphabet_chars_dict.

    :param char_occurrence_dict: Dictionary with char occurrence.
    :return: alphabet_chars_dict
    """
    error_raiser(char_occurrence_dict)
    alphabet_chars_dict.clear()
    for key, value in char_occurrence_dict.items():
        if key.isalpha():
            alphabet_chars_dict[key] = value
    return alphabet_chars_dict


def count_to_dictionary(text):
    """Check if char is in dictionary 'char_occurrence_dict'.

    If char is in 'char_occurrence_dict', then add 1 to its count.
    If char is not in 'char_occurrence_dict', then set its count to 1.
    :param text: Text from file or from user input.
    :return: char_counter
    """
    char_counter = 0
    for char in text:
        if char != "#":
            char_counter += 1
            if char in char_occurrence_dict:
                char_occurrence_dict[char] += 1
            else:
                char_occurrence_dict[char] = 1
    return char_counter


# Graf četnost znaků
def alphabet_occurrence_graph(alphabet_chars_dict):
    """Show table of char 'alphabet_chars_dict'.

    :param alphabet_chars_dict: Dictionary with letters
    :return: None
    """
    max_value = 0

    for key, value in alphabet_chars_dict.items():
        if value > max_value:
            max_value = value

    if max_value <= len("ČETNOST"):
        print("ZNAK|ČETNOST|NR.")
    else:
        print(f"ZNAK|ČETNOST{' ' * (max_value - len('ČETNOST'))}|NR.")

    for key, value in sorted(alphabet_chars_dict.items()):
        if max_value > len("ČETNOST"):
            print(f"   {key}|{'*' * value}{' ' * (max_value-value)}|{value}")
        else:
            print(f"   {key}|{'*' * value}{' ' * (len('ČETNOST')-value)}"
                  f"|{value}")


if __name__ == "__main__":
    main()
