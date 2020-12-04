import projekt

def test_dlzkystran():
    assert projekt.dlzkastrany(1,1,4,5) == 5.0
    assert projekt.dlzkastrany(1,1,2,1) == 1.0

def test_obvod():
    assert projekt.obvod(1,2,3)==6
    assert projekt.obvod(5,4,2) == 11
    assert projekt.obvod(12,23,30) == 65

def test_obsah():
    assert projekt.obsah(4,5,6) == 9.9216
    assert projekt.obsah(1,1,1) == 0.433

def test_zostrojenost():
    assert projekt.zostrojenost(3,4,5) == 1
    assert projekt.zostrojenost(1, 5 ,10) == 0

def test_pravouhlost():
    assert projekt.pravouhlost(3, 4,5)== 1
    assert projekt.pravouhlost(4, 4,4) == 0
