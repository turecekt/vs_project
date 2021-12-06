from main import * 

def test_encodovani_slovo():
    assert encodovani("AHOJ") == ".- .... --- .---"
    assert encodovani("LEON") == ".-.. . --- -."

def test_encodovani_veta():
    assert encodovani("MAM RAD PALACINKY") == "-- .- --  .-. .- -..  .--. .- .-.. .- -.-. .. -. -.- -.--"

def test_decodovani_znaky():
    assert decodovani(".-") == "A"
    assert decodovani("-...") == "B"
    assert decodovani("-.-.") == "C"

def test_decodovani_slovo():
    assert decodovani(".- .... --- .---") == "AHOJ"