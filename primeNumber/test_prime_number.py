from prime_number import is_prime_number

""" ahoj """


def test_is_prime_number_input_int():
    """ ahoj """
    desired_result = "3 je prvocislo"
    result = is_prime_number(3)
    assert result == desired_result
