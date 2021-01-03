from prime_number import is_prime_number


def test_is_prime_number_input_int():
    desired_result = "3 je prvocislo"
    result = is_prime_number(3)
    assert result == desired_result


