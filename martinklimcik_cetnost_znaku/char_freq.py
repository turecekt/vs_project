"""
Simple script which takes a text and prints out stats regarding character appearance frequency.
Input text is given either as path to a file with the text via command line parameter
or direct input if no parameter is given. Any additional parameters after first one are ignored.
Upper case and lower case letters are counted together.
Usage:
    python char_freq.py [path_to_file]
       - path_to_file absolute or relative path to the file containing text, optional parameter

ČETNOST ZNAKŮ
VSTUP
• Textový soubor (obsahující text bez diakritiky) jako parametr programu
• V případě spuštění bez parametru musí program umět zpracovat text ze
standardního vstupu až po řádek obsahující ukončovací symbol #
VÝSTUP
• Informace o celkovém počtu znaků
• Informace o nejčastějším znaku
• Informace o nejméně častém znaku
• Informace o průměrné četnosti
• Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)
"""
import sys
import string
from typing import List, AnyStr


def get_input() -> List[AnyStr]:
    """
    Get input text. If script was given any parameters, assumes the first one is path
    to a file with text, all other parameters are ignored. If no argument was given,
    ask user for input text cyclically until # symbol is given.
    Returns:
        List of string, each string representing one line of input
    """

    if len(sys.argv) > 1:
        # parameter given, try to open file path from first one, others are ignored
        try:
            with open(sys.argv[1], 'r') as input_file:
                return input_file.readlines()
        except FileNotFoundError:
            print(f'File "{sys.argv[1]}" was not found!')
            sys.exit(1)
    else:
        # No parameter given, wait for user input
        print('Input text to parse. May be multiple lines. End input with # symbol')
        values = []
        while True:
            user_input = input('')
            values.append(user_input)
            if '#' in user_input:
                return values


def char_frequency(text: str) -> None:
    """
    Counts and prints out stats about input text. Any non-english-alphabet characters
    will be ignored in stats (including spaces and newlines)
    Args:
        text: input text as a single string

    Returns:
        Prints out results
    """
    alphabet = {}
    for _c in text:
        char = _c.lower()  # Upper case letters are cast to lower case for simplicity
        if char in alphabet:  # increase character count if it is already present in dictionary
            alphabet[char] += 1
        elif char in string.ascii_lowercase:  # add to dictionary if it is part of english alphabet
            alphabet[char] = 1
    # get list of all letter counts and calculate relevant stats
    counts = [*alphabet.values()]
    if len(counts) == 0:
        print('Inputted text does not contain any tracked characters. No stats to print')
        return
    min_count = min(counts)
    max_count = max(counts)
    total_count = sum(counts)
    individual_chars = len(counts)
    average = total_count / individual_chars
    # get list of all characters with calculated min/max letter count
    min_chars = [char for char, count in alphabet.items() if count == min_count]
    max_chars = [char for char, count in alphabet.items() if count == max_count]

    def grammar_case(number: int) -> str:
        """
        Helper function for cleaner output - used to add 's' to make plural of nouns
        Args:
            number: number of occurrence(s) of whatever is printed out

        Returns:
            's' or empty string
        """
        return '' if number == 1 else 's'
    # print out stats
    print()
    print(f"The text contains {total_count} character{grammar_case(total_count)}.")
    print(f"There {'is' if individual_chars == 1 else 'are'} {individual_chars} "
          f"individual character{grammar_case(individual_chars)} from the alphabet, "
          f"average count per character being {average:.2f}")
    print(f"Least frequent character{grammar_case(len(min_chars))} "
          f"with {min_count} occurrence{grammar_case(min_count)}: {', '.join(min_chars)}")
    print(f"Most frequent character{grammar_case(len(max_chars))} "
          f"with {max_count} occurrence{grammar_case(max_count)}: {', '.join(max_chars)}")
    print('Frequency for each appearing character:')
    for char in string.ascii_lowercase:
        if char in alphabet:
            print(f' {char} : {alphabet[char]: >4}')


if __name__ == "__main__":
    INPUT_VALUES = ''.join(get_input())
    char_frequency(INPUT_VALUES)
