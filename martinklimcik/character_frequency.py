"""
Script to print out stats about character appearance frequency in text.

Input text is given either as path to a file  via command line parameter
or direct input if no parameter is given.
Any additional parameters after first one are ignored.
Upper case and lower case letters are counted together.
Usage:
    python char_freq.py [path_to_file]
       - path_to_file absolute or relative path to the file
                      containing text, optional parameter

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
from string import ascii_lowercase
from typing import List, AnyStr
import sys
import pytest


def get_file_content(filename: str) -> List[AnyStr]:
    """
    Get contents of a file.

    Args:
        filename: relative or absolute path to the file

    Returns:
        File lines as list of strings. None if file is not accessible.
    """
    try:
        with open(filename, 'r') as input_file:
            return input_file.readlines()
    except FileNotFoundError:
        return None


def get_input() -> str:
    """
    Get input text.

    If script was given any parameters, assumes the first one is path
    to a file with text, all other parameters are ignored.
    If no argument was given,
    ask user for input text cyclically until # symbol is given.
    Returns:
        List of string, each string representing one line of input
    """
    if len(sys.argv) > 1:
        # parameter given, try to open file path from first one
        result = get_file_content(sys.argv[1])
        if result is None:
            print(f'File "{sys.argv[1]}" was not found!')
            sys.exit(1)
    else:
        # No parameter given, wait for user input
        print('Write down text to parse. May be multiple lines. '
              'End input with # symbol')
        values = []
        while True:
            user_input = input('')
            values.append(user_input)
            if '#' in user_input:
                result = values
                break
    return ''.join(result)


def _grammar(number: int) -> str:
    """
    Add 's' to make plural of nouns if necessary.

    Used for output messages.

    Args:
        number: number of occurrence(s) of whatever is printed out

    Returns:
        's' or ''
    """
    return '' if number == 1 else 's'


def count_char_freq(text: str) -> {}:
    """
    Count frequency of characters for given text.

    Any non-english-alphabet (non-ascii) characters
    will be ignored (including spaces and newlines).
    Lowercase and uppercase are counted together.

    Args:
        text: input text as a single string

    Returns:
        Prints out results
    """
    alphabet = {}
    for _c in text:
        # Upper case letters are cast to lower case for simplicity
        char = _c.lower()
        if char in alphabet:
            # increase character count if it is already present in dictionary
            alphabet[char] += 1
        elif char in ascii_lowercase:
            # add to dictionary if it is part of english alphabet
            alphabet[char] = 1
    # get list of all letter counts and calculate relevant stats
    return alphabet


class CharStats:
    """Class containing calculated stats for further use."""

    all_chars = None  # dict with frequency of each alphabetical character
    total_count = None  # total number of characters
    min_count = None  # number of appearances of least frequent char
    max_count = None  # number of appearances of most frequent char
    unique_chars_count = None  # alphabet chars that appears at least once
    average = None  # averaged count per unique character
    min_chars = None  # list of least frequent chars
    max_chars = None  # list of most frequent chars
    missing_chars = []  # list of ascii chars that do not appear at all

    def __str__(self):
        """
        Printout values in understandable way.

        Returns:
            Resulting string
        """
        result = ''
        if CharStats is None:
            result += 'Inputted text does not contain any ' \
                      'tracked characters. No stats to show'
        else:
            result += f"The text contains {self.total_count} " \
                      f"character{_grammar(self.total_count)}.\n" \
                      f"There " \
                      f"{'is' if self.unique_chars_count == 1 else 'are'} " \
                      f"{self.unique_chars_count} individual " \
                      f"character{_grammar(self.unique_chars_count)} " \
                      f"from the alphabet, " \
                      f"average count per character being " \
                      f"{self.average:.2f}\n" \
                      f"Least frequent " \
                      f"character{_grammar(len(self.min_chars))} " \
                      f"with {self.min_count} " \
                      f"occurrence{_grammar(self.min_count)}: " \
                      f"{', '.join(self.min_chars)}\n" \
                      f"Most frequent " \
                      f"character{_grammar(len(self.max_chars))} " \
                      f"with {self.max_count} " \
                      f"occurrence{_grammar(self.max_count)}: " \
                      f"{', '.join(self.max_chars)}\n" \
                      "Frequency of each appearing character:\n"
            for char in ascii_lowercase:
                if char in self.all_chars:
                    result += f' {char} : {self.all_chars[char]: >4}\n'
            result += "Alphabet characters that do not appear at all: " \
                      f"{', '.join(self.missing_chars)}"
        return result


def calculate_stats(alphabet: dict) -> CharStats:
    """
    Calculate statistical values.

    Args:
        alphabet: dictionary with each item a single character
                  and value number of its appearances in text

    Returns:
        None if alphabet_dict is empty, otherwise a CharStats instance
    """
    s = CharStats()
    s.all_chars = alphabet
    counts = [*alphabet.values()]  # creates list of all values
    if len(counts) == 0:
        return None
    s.min_count = min(counts)
    s.max_count = max(counts)
    s.total_count = sum(counts)
    s.unique_chars_count = len(counts)
    s.average = s.total_count / s.unique_chars_count
    # get list of all characters with calculated min/max letter count
    s.min_chars = [c for c, cnt in alphabet.items() if cnt == s.min_count]
    s.max_chars = [c for c, cnt in alphabet.items() if cnt == s.max_count]
    # find which character are missing
    for char in ascii_lowercase:
        if char not in alphabet:
            s.missing_chars.append(char)
    return s


def test_open_file():
    """Test open_file method."""
    content = get_file_content('test_file_2')
    assert len(content) == 2
    assert all([a == b for a, b in zip(content, ['aaa', 'zzz'])])
    content = get_file_content('test_file_99')
    assert content is None


def test_count_char_freq():
    """Test count_char_freq method."""
    s = count_char_freq(''.join(get_file_content('test_file_2.txt')))
    assert s['a'] == 3
    assert s['z'] == 3
    s = count_char_freq('The Test\n 123456 t')
    assert s['t'] == 4
    assert s['h'] == 1
    assert s['e'] == 2
    assert s['s'] == 1


def test_calculate_stats():
    """Test calculate_stats method."""
    s = calculate_stats(count_char_freq(
        ''.join(get_file_content('test_file_1.txt'))))
    assert s.total_count == 2231
    assert s.unique_chars_count == 20
    assert s.average == pytest.approx(111.55, 0.01)
    assert s.min_count == 22
    assert s.min_chars == ['q', 'f', 'h']
    assert s.max_count == 244
    assert s.max_chars == ['e']
    assert s.all_chars['t'] == 175
    assert s.all_chars['c'] == 92
    assert s.missing_chars == ['j', 'k', 'w', 'x', 'y', 'z']


if __name__ == "__main__":
    INPUT_VALUES = get_input()
    freq = count_char_freq(INPUT_VALUES)
    stats = calculate_stats(freq)
    print(stats)
