from translator import encode, decode


def test_encode():
    assert encode('test') == '- . ... - '


def test_decode():
    assert decode('- . ... - ') == 'test'
