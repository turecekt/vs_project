"""Unit test for prime number program."""
import main


def test_input():
    """Test for input."""
    assert main.check_number("100") is True
    assert main.check_number("10.2") is False
    assert main.check_number("string") is False


def test_check_prime_number():
    """Test for normal method to check if number is prime."""
    assert main.check_prime_number(1) is False
    assert main.check_prime_number(12) is False
    assert main.check_prime_number(3) is True
    assert main.check_prime_number(17) is True


def test_prime_number_fermat_test():
    """Test for fermat test method to check if number is prime."""
    assert main.fermat_test(2, 3) is True
    assert main.fermat_test(44207, 3) is True
    assert main.fermat_test(211507, 3) is True
    assert main.fermat_test(167340, 3) is False
    assert main.fermat_test(732169, 3) is True
    assert main.fermat_test(732630, 3) is False


def test_higher_number():
    """Test if number is higher then 100."""
    assert main.check_higher_number(10) is False
    assert main.check_higher_number(154) is True
    assert main.check_higher_number(101) is True
    assert main.check_higher_number(57) is False
