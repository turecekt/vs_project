"""Ahoj."""
from prime_number import is_prime_number, check_input


def test_is_prime_number_input_int():
    """Ahoj."""
    desired_result = "3 je prvocislo"
    result = is_prime_number(3)
    assert result == desired_result


def test_is_prime_number_input_float():
    """Ahoj."""
    desired_result = "3.0 je prvocislo"
    result = is_prime_number(3.0)
    assert result == desired_result


def test_is_prime_number_input_string():
    """Ahoj."""
    desired_result = "Toto neni cislo"
    result = check_input("string")
    assert result == desired_result


def test_is_prime_number_input_null():
    """Ahoj."""
    desired_result = "Toto neni cislo"
    result = check_input()
    assert result == desired_result


def test_is_prime_number_input_char():
    """Ahoj."""
    desired_result = "Toto neni cislo"
    result = check_input('c')
    assert result == desired_result
