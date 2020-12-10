import morse_code


def test_encrypt():
    assert morse_code.encrypt('T T') == '-  -'
    assert morse_code.encrypt('test') == '- . ... -'


def test_decrypt():
    assert morse_code.decrypt('.- -- -... .. - .. --- ..- ...') == 'AMBITIOUS'
    assert morse_code.decrypt('..- - -...  .--- .  ... -.- ...- . .-.. .-  ..- -. .. ...- . .-. --.. .. - .-') \
           == 'UTB JE SKVELA UNIVERZITA'
