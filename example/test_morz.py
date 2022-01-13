import morz


def test_kod():
    assert morz.kod('A') == '.- '
    assert morz.kod('AHOJ SVETE.') == '.- .... --- .---  ... ...- . - . .-.-.-'
    assert morz.kod('GRANKO') == '--. .-. .- -. -.- --- '
    assert morz.kod('KRECEK MIRECEK DOSEL A NEPOSEL') == """-.- .-. . -.-. . -.-  -- ..
    .-. . -.-. . -.-  -.. --- ... . .-..  .-  -. . .--. --- ... . .-.. """


def test_dekod():
    assert morz.dekod('.-') == 'A'
    assert morz.dekod('.- .... --- .---  ... ...- . - . .-.-.- ') == """AHOJ
    SVETE."""
    assert morz.dekod('--. .-. .- -. -.- --- ') == 'GRANKO '
    assert morz.dekod("""-.- .-. . -.-. . -.-  -- .. .-. . -.-. . -.-  -.. ---
                      ... . .-..  .-  -. . .--. --- ... . .-.. """) == """KRECEK
    MIRECEK DOSEL A NEPOSEL"""
