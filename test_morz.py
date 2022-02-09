import morz


def test_kod():
    assert morz.kod('A') == '.- '
    assert morz.kod('AHOJ') == '.- .... --- .--- '
    assert morz.kod('GRANKO') == '--. .-. .- -. -.- --- '


def test_dekod():
    assert morz.dekod('.-') == 'A'
    assert morz.dekod('.- .... --- .---') == 'AHOJ'
    assert morz.dekod('--. .-. .- -. -.- ---') == 'GRANKO'
