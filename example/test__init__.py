import __init__


def test_nacti_text_seZnakem():
    assert __init__.nacti_text('basnicka_seznakem.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí'   # noqa


def test_nacti_text_bezZnaku():
    assert __init__.nacti_text('basnicka_bezznaku.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí a tady už nám text končí a už dál vlastně vůbec nepokračuje.'  # noqa


def test_nacti_text_znakNaZacatku():
    assert __init__.nacti_text('basnicka_nazacatku.txt') == None    # noqa


def test_uprav_text():
    assert __init__.uprav_text('Toto je   básnička.') == 'totojebásnička.'


def test_zjisti_cetnosti():
    assert __init__.zjisti_cetnosti('basnicka_ha.txt') == {'h': 3, 'a': 3}


def test_pocet_ruznych_znaku():
    assert __init__.pocet_ruznych_znaku([('a', 5), ('b', 3), ('c', 1)]) == 3


def test_nejcetnejsi_znaky():
    assert __init__.nejcetnejsi_znaky({'h': 3, 'a': 2}) == 'h'


def test_nejcetnejsi_znaky_2stejne():
    assert __init__.nejcetnejsi_znaky({'h': 3, 'a': 2, 'c': 3}) == 'h'


def test_nejmenecetne_znaky():
    assert __init__.nejmenecetne_znaky({'h': 3, 'a': 2}) == 'a'


def test_nejmenecetne_znaky_2stejne():
    assert __init__.nejmenecetne_znaky({'h': 3, 'a': 2, 'd': 2}) == 'a'
