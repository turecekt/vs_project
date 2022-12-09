from main import char_min_values, char_max_values, char_average, occurrence_to_alphabetic_dict, count_to_dictionary
import pytest

dict_test = {"a": 2, "b": 1, "c": 1, "d": 3, "e": 3, "f": 3}
text_test = "abcdadedeefff"

# nainstalovat pytest a pytest-cov
# spouštění testu:>> pytest
# test coverage:>> pytest --cov

# TODO Unit testy
# TODO Docstrings
# TODO kontrola pomocí flake8 a flake8-docstrings


def test_char_min_values():
    """Test function minimum values of chars"""
    assert char_min_values(dict_test) == ["b", "c"]
    assert char_min_values({"a": 1}) == ["a"]

    with pytest.raises(TypeError):
        char_min_values(True)
        char_min_values(5 + 3j)
        char_min_values("ahoj")


def test_char_max_values():
    """Test function maximum values of chars"""
    assert char_max_values(dict_test) == ["d", "e", "f"]
    assert char_max_values({"a": 1}) == ["a"]

    with pytest.raises(TypeError):
        char_min_values(False)
        char_min_values(2 + 3j)
        char_min_values("ahoj")


def test_char_average():
    """Test function average value of chars"""
    assert char_average(dict_test) == 2.17
    assert char_average({"a": 1}) == 1

    with pytest.raises(TypeError):
        char_average(True)
        char_average(9 + 1j)
        char_average("ahoj")


def test_occurrence_to_alphabetic_dict():
    """Test function occurrence of chars"""
    #TODO upravit ↓
    # assert occurrence_to_alphabetic_dict(dict_test) == {'a': 2, 'b': 1, 'c': 1, 'd': 3, 'e': 3, 'f': 3}
    assert occurrence_to_alphabetic_dict({"a": 1}) == {"a": 1}

    with pytest.raises(TypeError):
        occurrence_to_alphabetic_dict(True)
        occurrence_to_alphabetic_dict(6 + 6j)
        occurrence_to_alphabetic_dict("ahoj")


def test_count_to_dictionary():
    #TODO pridat raiser
    """Test function count_to_dictionary"""
    assert count_to_dictionary(text_test) == 13
    assert count_to_dictionary({"a": 1}) == 1