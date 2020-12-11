import morse_code


def test_encrypt():
    assert morse_code.encrypt('T T') == '-  -'
    assert morse_code.encrypt('test') == '- . ... -'
    assert morse_code.encrypt('33 -  10 = 23') == \
           '...-- ...--  -....-   .---- -----  -...-  ..--- ...--'
    assert morse_code.encrypt('/+-: .    .') == \
           '-..-. .-.-. -....- ---...  .-.-.-     .-.-.-'
    assert morse_code.encrypt('1234567890') == \
           '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----'
    assert morse_code.encrypt('This project was created for educational '
                              'purposes. I am testing longer '
                              'string to see multiple lines '
                              'of output. ') == \
           '- .... .. ...  .--. .-. --- .--- . -.-. -  .-- .- ... ' \
           ' -.-. .-. . .- - . -..  ..-. --- .-.  . -.. ..- -.-. ' \
           '.- - .. --- -. .- .-..  .--. ..- .-. .--. --- ... . ' \
           '... .-.-.-  ..  .- --  - . ... - .. -. --.  .-.. --- ' \
           '-. --. . .-.  ... - .-. .. -. --.  - ---  ... . .  -- ' \
           '..- .-.. - .. .--. .-.. .  .-.. .. -. . ...  --- ..-. ' \
           ' --- ..- - .--. ..- - .-.-.- '


def test_decrypt():
    assert morse_code.decrypt('- -... ..-  .. ...  --. .-. '
                              '. .- -  ..- -. .. ...- . .-. '
                              '... .. - -.-- .-.-.-') \
           == 'TBU IS GREAT UNIVERSITY.'
    assert morse_code.decrypt('...-- ...--  -....-   .---- '
                              '-----  -...-  ..--- ...--') \
           == '33 - 10 = 23'
    assert morse_code.decrypt('-..-. .-.-. -....- ---...  '
                              '.-.-.-     .-.-.-') \
           == '/+-: . .'
    assert morse_code.decrypt('.---- ..--- ...-- ....- ..... '
                              '-.... --... ---.. ----. -----') \
           == '1234567890'
