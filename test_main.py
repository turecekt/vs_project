import main


def test_nacti_text_seZnakem():
    assert main.nacti_text('basnicka_seznakem.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí'   # noqa


def test_nacti_text_bezZnaku():
    assert main.nacti_text('basnicka_bezznaku.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí a tady už nám text končí a už dál vlastně vůbec nepokračuje.'  # noqa


def test_nacti_text_znakNaZacatku():
    assert main.nacti_text('basnicka_nazacatku.txt') == None    # noqa


def test_uprav_text():
    assert main.uprav_text('Toto je   básnička.') == 'totojebásnička.'


def test_zjisti_cetnosti():
    assert main.zjisti_cetnosti('basnicka_ha.txt') == {'h': 3, 'a': 3}


def test_pocet_ruznych_znaku():
    assert main.pocet_ruznych_znaku([('a', 5), ('b', 3), ('c', 1)]) == 3


def test_nejcetnejsi_znaky():
    assert main.nejcetnejsi_znaky({'h': 3, 'a': 2}) == 'h'


def test_nejcetnejsi_znaky_2stejne():
    assert main.nejcetnejsi_znaky({'h': 3, 'a': 2, 'c': 3}) == 'h'


def test_nejmenecetne_znaky():
    assert main.nejmenecetne_znaky({'h': 3, 'a': 2}) == 'a'


def test_nejmenecetne_znaky_2stejne():
    assert main.nejmenecetne_znaky({'h': 3, 'a': 2, 'd': 2}) == 'a'
