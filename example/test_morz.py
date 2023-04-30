"""Unit test modul pro Morzeovu abecedu."""

import morz


def test_kod():
    """Test funkce kod."""
    assert morz.kod('A') == '.- '
    assert morz.kod('AHOJ') == '.- .... --- .--- '
    assert morz.kod('GRANKO') == '--. .-. .- -. -.- --- '


def test_dekod():
    """Test funkce dekod."""
    assert morz.dekod('.-') == 'A'
    assert morz.dekod('.- .... --- .---') == 'AHOJ'
    assert morz.dekod('--. .-. .- -. -.- ---') == 'GRANKO'
