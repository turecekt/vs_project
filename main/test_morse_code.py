# Unit tests for Python program to implement Morse Code Translator

"""

This module consist of two methods for unit testing.
Methods compare matching of string and morse code.
"""

import morse_code


def test_encrypt():
    """Function test_encrypt() compares given string with morse code.
            """
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
    """Function test_decrypt() compares given morse code with string.
                """
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
