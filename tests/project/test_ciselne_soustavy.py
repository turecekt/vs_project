from project.ciselne_soustavy import is_number_int
from project.ciselne_soustavy import number_conversion
import pytest


class TestIsNumberInt:
    @pytest.mark.parametrize("number", ["0", "5", "55", "444", "065", "66.0", "0.0", "066.0", "-5"])
    def test_true(self, number):
        result = is_number_int(number)

        assert result is True

    @pytest.mark.parametrize("number", ["a", "5a", "55.5", "55.a", "a5", "-5.6"])
    def test_false(self, number):
        result = is_number_int(number)

        assert result is False


class TestNumberConversion:
    @pytest.mark.parametrize(
        "number, number_system, expected",
        [
            (2, 4, "2"),
            (4, 2, "100"),
            (1, 30, "1"),
            (35, 36, "Z"),
            (46655, 36, "ZZZ"),
            (0, 6, "0"),
            (55, 10, "55"),
        ],
    )
    def test_ok(self, number, number_system, expected):
        result = number_conversion(number, number_system)

        assert result == expected

# tadeaskuv test
# def fnc():
#     a = input()
#     b = input()
#     return (a, b)
#
# def test_input(mocker):
#     mocker.patch("builtins.input", side_effect=["a", "b"])
#
#     assert ["a", "b"] == fnc()
