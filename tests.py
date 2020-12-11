"""Unit testy."""

import morse


def test_sifrovani():
    """Unit test.

    test na funkci sifrovani()
    """
    ocekavany_vystup = "- . ... - "
    assert sifrovani("test") == ocekavany_vystup
    assert sifrovani("test s mezerami") == \
           "- . ... -  ...  -- . --.. . .-. .- -- .. "
    assert sifrovani("1, 2, 3, 4") == \
           ".---- --..--  ..--- --..--  ...-- --..--  ....- "
    assert sifrovani(". , () ? !") == \
           ".-.-.-  --..--  -.--. -.--.-  ..--..  -.-.-- "


def test_desifrovani():
    """Unit test.

    test na funkci desifrovani()
    """
    vstup = "- . ... -"
    ocekavany_vystup = "TEST"
    assert desifrovani(vstup) == ocekavany_vystup
    assert desifrovani("- . ... -  ...  -- . --.. . .-. .- -- ..") == \
           "test s mezerami".upper()
    assert desifrovani(".---- --..--  ..--- --..--  ...-- --..--  ....-") \
           == "1, 2, 3, 4"
    assert desifrovani(".-.-.-  --..--  -.--. -.--.-  ..--..  -.-.--") == \
           ". , () ? !"


test_sifrovani()
test_desifrovani()

