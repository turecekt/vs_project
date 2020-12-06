import __init__


def test_nacti_text_seZnakem():
    assert __init__.nacti_text('basnicka_seznakem.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí'

def test_nacti_text_bezZnaku():
    assert __init__.nacti_text('basnicka_bezznaku.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí a tady už nám text končí a už dál vlastně vůbec nepokračuje.'

def test_nacti_text_znakNaZacatku():
    assert __init__.nacti_text('basnicka_nazacatku.txt') == None
    
def test_uprav_text():
    assert __init__.uprav_text('Toto je básnička') == 'totojebásnička'