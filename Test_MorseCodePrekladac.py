# Pytest MorseCodePrekladac
from MorseCodePrekladac import sifrovani, desifrovani

def test_sifrovani1():
    # Testování překladu do abecedy z morseovky 
    assert sifrovani("AHOJ!") == ".- .... --- .--- -.-.--"
    assert sifrovani("733290807") == "--... ...-- ...-- ..--- ----. ----- ---.. ----- --..."
    assert sifrovani("ME ZE RY") == "-- . | --.. . | .-. -.--"

def test_desifrovani1():
    # Testování překladu z morseovky do abecedy
    assert desifrovani("--.. -.. .-. .- ...- .. --") == "ZDRAVIM"
    assert desifrovani("-.... ----- ..... ---.. ----. ..--- ----- ----- ---..") == "605892008"
    assert desifrovani("-- . | --.. . | .-. -.--") == "ME ZE RY"