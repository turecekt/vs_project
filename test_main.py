"""Unit Testy."""
from main import (
    char_min_values,
    char_max_values,
    char_average,
    occurrence_to_alphabetic_dict,
    count_to_dictionary
)
import pytest

dict_test = {"a": 2, "b": 1, "c": 1, "d": 3, "e": 3, "f": 3, "1": 1, "2": 2}
text_test = "abcdadedeefff"


@pytest.mark.parametrize("expected_exception, hodnota", [(TypeError, True),
                                                         (TypeError, 5 + 6j),
                                                         (TypeError, "ahoj")])
def test_char_min_values(expected_exception, hodnota):
    """Test function minimum values of chars."""
    assert char_min_values(dict_test) == ["b", "c", "1"]
    assert char_min_values({"a": 1}) == ["a"]
    with pytest.raises(expected_exception):
        char_min_values(hodnota)


@pytest.mark.parametrize("expected_exception, hodnota", [(TypeError, True),
                                                         (TypeError, 5 + 6j),
                                                         (TypeError, "ahoj")])
def test_char_max_values(expected_exception, hodnota):
    """Test function maximum values of chars."""
    assert char_max_values(dict_test) == ["d", "e", "f"]
    assert char_max_values({"a": 1}) == ["a"]
    with pytest.raises(expected_exception):
        char_min_values(hodnota)


@pytest.mark.parametrize("expected_exception, hodnota", [(TypeError, True),
                                                         (TypeError, 5 + 6j),
                                                         (TypeError, "ahoj")])
def test_char_average(expected_exception, hodnota):
    """Test function average value of chars."""
    assert char_average(dict_test) == 2.00
    assert char_average({"a": 1}) == 1

    with pytest.raises(expected_exception):
        char_average(hodnota)


@pytest.mark.parametrize("expected_exception, hodnota", [(TypeError, True),
                                                         (TypeError, 5 + 6j),
                                                         (TypeError, "ahoj")])
def test_occurrence_to_alphabetic_dict(expected_exception, hodnota):
    """Test function occurrence of chars."""
    assert occurrence_to_alphabetic_dict(dict_test) == \
           {'a': 2, 'b': 1, 'c': 1, 'd': 3, 'e': 3, 'f': 3}
    assert occurrence_to_alphabetic_dict({"a": 1}) == {'a': 1}

    with pytest.raises(TypeError):
        occurrence_to_alphabetic_dict(hodnota)


def test_count_to_dictionary():
    """Test function count_to_dictionary."""
    assert count_to_dictionary(text_test) == 13
    assert count_to_dictionary({"a": 1}) == 1
