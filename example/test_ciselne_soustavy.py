from ciselne_soustavy import is_number_int
import pytest


@pytest.mark.parametrize("number"["0", "5", "55", "444", "065", "66.0", "0.0", "066.0"])
def test_is_number_int_true(number):
    result = is_number_int(number)

    assert result is True


@pytest.mark.parametrize("number", ["a", "5a", "55.5", "-5", "55.a", "a5"])
def test_is_number_int_false(number):
    result = is_number_int(number)

    assert result is False
