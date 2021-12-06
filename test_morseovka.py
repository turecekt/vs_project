"""Test morse."""

from main import encodovani, decodovani


def test_encodovani_slovo():
    """Test encodovani."""
    assert encodovani("AHOJ") == ".- .... --- .---"
    assert encodovani("LEON") == ".-.. . --- -."


def test_encodovani_veta():
    """Test encodovani."""
    assert encodovani("MAM RAD PALACINKY") == "-- .- --  .-. .- -..  .--." \
                                              " .- .-.. .- -.-. .. -. -.- -.--"


def test_decodovani_znaky():
    """Test decodovani."""
    assert decodovani(".-") == "A"
    assert decodovani("-...") == "B"
    assert decodovani("-.-.") == "C"


def test_decodovani_slovo():
    """Test decodovani."""
    assert decodovani(".- .... --- .---") == "AHOJ"
