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

Tests:
>>> test_open_file()
>>> test_input()
>>> test_count_char_freq()
>>> test_calculate_stats()
"""
from string import ascii_uppercase
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


def get_input(filename: str = None) -> str:
    """
    Get input text.

    If script was given any parameters, assumes the first one is path
    to a file with text, all other parameters are ignored.
    If no argument was given,
    ask user for input text cyclically until # symbol is given.
    Priority order for input:
        1. filename given as parameter to this method
        2. filename given as script parameter
        3. user input
    Args:
        filename - optional, name of file to open.

    Returns:
        List of string, each string representing one line of input
    """
    _file = None
    if filename is not None:
        # method parameter given, try to open file
        result = get_file_content(filename)
        _file = filename
    elif len(sys.argv) > 1:
        # script parameter given, try to open file path from first one
        result = get_file_content(sys.argv[1])
        _file = sys.argv[1]
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
    if result is None:
        print(f'File "{_file}" was not found!')
        sys.exit(1)
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
        char = _c.upper()
        if char in alphabet:
            # increase character count if it is already present in dictionary
            alphabet[char] += 1
        elif char in ascii_uppercase:
            # add to dictionary if it is part of english alphabet
            alphabet[char] = 1
    # get list of all letter counts and calculate relevant stats
    return alphabet


class CharStats:
    """Class containing calculated stats for further use."""

    def __init__(self):
        """Initialise default values."""
        self.all_chars = None  # dict with frequency of each alphabetical char
        self.total_count = None  # total number of characters
        self.min_count = None  # number of appearances of least frequent char
        self.max_count = None  # number of appearances of most frequent char
        self.unique_chars_count = None  # count chars appearing at least once
        self.average = None  # averaged count per unique character
        self.min_chars = None  # list of least frequent chars
        self.max_chars = None  # list of most frequent chars
        self.missing_chars = []  # list of ascii chars not present at all

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
            for char in ascii_uppercase:
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
    for char in ascii_uppercase:
        if char not in alphabet:
            s.missing_chars.append(char)
    return s


# === Unit Tests ===
TEST_FILE_1 = 'test_file_1.txt'
TEST_FILE_2 = 'test_file_2.txt'
TEST_FILE_INVALID = 'test_file_99.txt'


def _eq(actual, expected) -> None:
    """
    Assert equal with more reasonable output on failure.

    Args:
        actual: value to compare
        expected: expected value

    Returns:
        Raises AssertionError if actual does not equal expected
    """
    assert actual == expected, f'\nActual:   "{actual}" ({type(actual)})\n' \
                               f'Expected: "{expected}" {type(expected)})'


def test_open_file():
    """Test open_file method."""
    # Open file
    content = get_file_content(TEST_FILE_2)
    _eq(len(content), 2)
    _eq(content, ['aaa\n', 'zzz'])
    # Try open non-existent file
    content = get_file_content(TEST_FILE_INVALID)
    assert content is None


def test_input():
    """Test get_input method."""
    content = get_input(TEST_FILE_2)
    _eq(content, 'aaa\nzzz')


def test_count_char_freq():
    """Test count_char_freq method."""
    # count character frequency of test file
    s = count_char_freq(get_input(TEST_FILE_2))
    _eq(s['A'], 3)
    _eq(s['Z'], 3)
    # count char freq of directly given text
    s = count_char_freq('The Test\n 123456 t')
    _eq(s['T'], 4)
    _eq(s['H'], 1)
    _eq(s['E'], 2)
    _eq(s['S'], 1)


def test_calculate_stats():
    """Test calculate_stats method."""
    # Calculate stats of input from test file
    s = calculate_stats(count_char_freq(get_input(TEST_FILE_1)))
    _eq(s.total_count, 2231), f"{s.total_count}"
    _eq(s.unique_chars_count, 20)
    _eq(s.average, pytest.approx(111.55, 0.01))
    _eq(s.min_count, 22)
    _eq(s.min_chars, ['Q', 'F', 'H'])
    _eq(s.max_count, 244)
    _eq(s.max_chars, ['E'])
    _eq(s.all_chars['T'], 175)
    _eq(s.all_chars['C'], 92)
    _eq(s.missing_chars, ['J', 'K', 'W', 'X', 'Y', 'Z'])
    print(s)


# === Run script - only when not imported ===
if __name__ == "__main__":
    INPUT_VALUES = get_input()
    freq = count_char_freq(INPUT_VALUES)
    stats = calculate_stats(freq)
    print(stats)
