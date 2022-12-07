from main import char_min_values
import pytest

dict_test = {"a": 2, "b": 1, "c": 1, "d":3}
text_test = "abcdadd"

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
        char_min_values(5+3j)
        char_min_values("ahoj")

def test_char_max_values():
    # TODO
    pass

def test_char_average():
    #TODO
    pass

def test_occurrence_to_alphabetic_dict():
    #TODO
    pass

def test_count_to_dictionary():
    #TODO
    pass