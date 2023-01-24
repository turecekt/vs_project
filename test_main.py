"""
Testovací modul k main.py.

@author: psantler
"""
import main
import pytest
from io import StringIO

numbers_input = [1, 5, 9, 6, 3, 8, 2, 7, 4]
numbers_input_pseudorandom = main.generate_pseoudorandom_array(
    main.ARRAY_LEGTH, main.GROUND_VALUE, main.TOP_VALUE)


def test_input_file(get_file_numbers):
    """
    Test kontrolující správnost zadaných dat v souboru.

    :param get_file_numbers: soubor s testovacími daty
    """
    assert get_file_numbers == [1, 4, 5, 6, 8, 3, 9, 7, 2]


def test_generate_pseudorandom():
    """Test kontrolující generování náhodných čísel."""
    x = 0
    while x < 100:
        assert numbers_input_pseudorandom != main.generate_pseoudorandom_array(
            main.ARRAY_LEGTH, main.GROUND_VALUE, main.TOP_VALUE)
        x += 1


def test_bubble_sort(get_file_numbers):
    """Test kontrolující funkčnost bubbble sortu.
    Pro kontrolu používá pevnou sadu testovacích dat,
    soubor s předvolenou testovací sadou a nádohně
    generovanou testovací sadu.
    
    :param get_file_numbers: soubor s testovacími daty
    """
    list_numbers_input_pseudorandom = sorted(numbers_input_pseudorandom)
    list_merged = main.bubble_sort(numbers_input_pseudorandom)
    assert list_merged == list_numbers_input_pseudorandom

    list_merged = main.bubble_sort(numbers_input)
    assert list_merged == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    list_merged = main.bubble_sort(get_file_numbers)
    assert list_merged == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_merge_sort(get_file_numbers):
    """Test kontrolující funkčnost merge sortu.
    Pro kontrolu používá pevnou sadu testovacích dat,
    soubor s předvolenou testovací sadou a nádohně
    generovanou testovací sadu.
    
    :param get_file_numbers:  soubor s testovacími daty
    """
    list_numbers_input_pseudorandom = sorted(numbers_input_pseudorandom)
    list_merged = main.merge_sort(numbers_input_pseudorandom)
    assert list_merged == list_numbers_input_pseudorandom

    list_merged = main.merge_sort(numbers_input)
    assert list_merged == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    list_merged = main.merge_sort(get_file_numbers)
    assert list_merged == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_insertion_sort(get_file_numbers):
    """Test kontrolující funkčnost insertion sortu.
    Pro kontrolu používá pevnou sadu testovacích dat,
    soubor s předvolenou testovací sadou a
    nádohně generovanou testovací sadu.

    :param get_file_numbers:
    """

    list_numbers_input_pseudorandom = sorted(numbers_input_pseudorandom)
    list_merged = main.insertion_sort(numbers_input_pseudorandom)
    assert list_merged == list_numbers_input_pseudorandom

    list_merged = main.insertion_sort(numbers_input)
    assert list_merged == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    list_merged = main.insertion_sort(get_file_numbers)
    assert list_merged == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_lowest_num(sort_numbers):
    """Test kontrolující funkčnost hledání nejmenšího čísla.

    :param sort_numbers: seřazená čisla
    """
    assert main.get_lowest_num(sort_numbers) == 1


def test_highest_num(sort_numbers):
    """Test kontrolující funkčnost hledání největšího čísla.

    :param sort_numbers: seřazená čísla
    """
    assert main.get_highest_num(sort_numbers) == 9


def test_sort_numbers(monkeypatch):
    """Test kontrolující funkčnost výběru typu sortu.
    Nejprve proběhne inicializace user inputu,
    poté jeho simulace, nakonec se spustí samotná
    funkce se simulovaným inputem.

    :param monkeypatch: monkeypatch simuluje user input v průběhu testu
    """
    number_inputs = StringIO('1')
    monkeypatch.setattr('sys.stdin', number_inputs)
    output = main.sort_numbers(numbers_input)

    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    number_inputs = StringIO('2')
    monkeypatch.setattr('sys.stdin', number_inputs)
    output = main.sort_numbers(numbers_input)

    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    number_inputs = StringIO('3')
    monkeypatch.setattr('sys.stdin', number_inputs)
    output = main.sort_numbers(numbers_input)

    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.fixture
def get_file_numbers(monkeypatch):
    """Fixture díky níž načítáme data ze souboru.

    :param monkeypatch: monkeypatch simuluje user input v průběhu testu
    :return:
    """
    numbers_inputs = StringIO("numbers.txt")
    monkeypatch.setattr("sys.stdin", numbers_inputs)
    filename = input("get file")

    file = main.input_file(filename)
    return file


@pytest.fixture
def sort_numbers(get_file_numbers):
    """Fixture.
    Díky níž sortujeme čísla pomocí předem definované sort
    funkce jazyka python pro kontrolu v dalších testech.
    
    :param get_file_numbers:
    :return:
    """
    return sorted(get_file_numbers)
