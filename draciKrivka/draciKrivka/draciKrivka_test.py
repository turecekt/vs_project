"""draciKrivka_test"""

from draciKrivka import vrat_cislo

def test_vrat_cislo_spravne():
    """Test vraceni spravneho cisla."""
    assert vrat_cislo("10") == 10
    assert vrat_cislo("0") == 0

def test_vrat_cislo_zaporne():
    """Test vraceni zaporneho cisla."""
    assert vrat_cislo("-10") == 10
    assert vrat_cislo("-0") == 0


def test_vrat_cislo_chybny_vstup():
    """Test vraceni chybneho vstupu cisla."""
    assert vrat_cislo("sdfe") == 9
    assert vrat_cislo("slovo") == 9
    assert vrat_cislo("") == 9
    assert vrat_cislo("7.6") == 9

