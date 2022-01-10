from import text_do_mors, mors_do_text

pole = "priklad"
text = "priklad1"
mors = "priklad2"
zprava = "priklad3"
response = "1" or "2"


def test_main_chec_text_do_mors():
    text_do_mors(pole)
    mors_do_text(pole)
    mors_do_text(mors)
    text_do_mors(text)
    mors_do_text(text)
    text_do_mors(mors)
    text_do_mors(zprava)
    mors_do_text(zprava)
    mors_do_text(response)
    text_do_mors(response)


def test_main_chec_mors_do_text():
    text_do_mors(pole)
    mors_do_text(pole)
    mors_do_text(mors)
    text_do_mors(text)
    mors_do_text(text)
    text_do_mors(mors)
    text_do_mors(zprava)
    mors_do_text(zprava)
    mors_do_text(response)
    text_do_mors(response)
