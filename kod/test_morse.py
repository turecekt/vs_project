"""Importovanie zdrojoveho kodu."""

import morse


def test_encrypt():
    """Overenie toho, ze prekladac dokaze prelozit individualne znaky."""
    assert morse.encryptor('A') == '.- '

    """Overenie toho, ze prekladac dokaze prelozit cele slova."""
    assert morse.encryptor('SKUSKA2') == '... -.- ..- ... -.- .- ..--- '

    """Overenie toho, ze prekladac dokaze prelozit medzery v texte."""
    assert morse.encryptor('M E D Z E R E') \
           == '-- | . | -.. | --.. | . | .-. | . '

    """Overenie toho, ze prekladac dokaze prelozit symboly v texte."""
    assert morse.encryptor(',?YM80LY/') \
           == '--..-- ..--.. -.-- -- ---.. ----- .-.. -.-- -..-. '

    """Overenie toho, ze prekladac dokaze prelozit cele vety pisane
    pomocou malych pismen)"""
    assert morse.encryptor('male na velke') \
           == '-- .- .-.. . | -. .- | ...- . .-.. -.- . '


def test_decrypt():
    """Preklad znakov z Morse Kodu do abecedy."""
    assert morse.decryptor('.-') == 'A'

    """Preklad slov z Morse Kodu do abecedy."""
    assert morse.decryptor('... .-.. --- ...- ---') == 'SLOVO'

    """Preklad symbolov z Morse Kodu do abecedy."""
    assert morse.decryptor('..--.. -..-. -....- .-.-.-') == '?/-.'
