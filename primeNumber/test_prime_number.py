"""Test class for whole application."""
from prime_number import is_prime_number, check_input


def test_is_prime_number_input_int_is_prime():
    """Test for int input which is prime number."""
    desired_result = "3 is prime number."
    result = is_prime_number(3)
    assert result == desired_result


def test_is_prime_number_input_int_is_not_prime():
    """Test for int input which is not prime number."""
    desired_result = "6 is not prime number."
    result = is_prime_number(6)
    assert result == desired_result


def test_is_prime_number_input_string():
    """Test for string input."""
    desired_result = "This is not a number!"
    result = check_input("string")
    assert result == desired_result


def test_is_prime_number_input_no():
    """Test for no input."""
    desired_result = "This is not a number!"
    result = check_input("")
    assert result == desired_result


def test_is_prime_number_input_char():
    """Test for char input."""
    desired_result = "This is not a number!"
    result = check_input('c')
    assert result == desired_result
