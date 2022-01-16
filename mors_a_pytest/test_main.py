"""Text."""
from Main import text_do_mors, mors_do_text, main


pole = "priklad"

"""Text."""
def test_main_chec_text_do_mors():
    text_do_mors(pole)


"""Text."""
def test_main_chec_mors_do_text():
    mors_do_text(pole)


"""Text."""
def test_mors_do_text1():
    mors1 = "... --- ..."
    assert mors_do_text
    ("S O S") == mors1


"""Text."""
def test_text_do_mors1():
    text1 = "S O S"
    assert text_do_mors
    ("... --- ...") == text1


"""Text."""
def test_main():
    response = "1"
    assert main
    ("Napiste morseovku (s mezerou mezi kazdym pismenem): ") == response


"""Text."""
def test_main2():
    response2 = "2"
    assert main
    ("Napište text: ") == response2
