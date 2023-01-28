# pytest pre funkciu 'prvocislo'

from main import prvocislo


def test_prvocislo():
    assert prvocislo(1) is False
    assert prvocislo(2) is True
    assert prvocislo(3) is True
    assert prvocislo(4) is False
    assert prvocislo(5) is True
    assert prvocislo(6) is False
    assert prvocislo(149) is True
    assert prvocislo(151) is True
    assert prvocislo(317) is True
    assert prvocislo(577) is True
    assert prvocislo(977) is True
    assert prvocislo(983) is True
    assert prvocislo(991) is True
    assert prvocislo(919) is True
    assert prvocislo(929) is True
    assert prvocislo(937) is True
    assert prvocislo(983) is True
