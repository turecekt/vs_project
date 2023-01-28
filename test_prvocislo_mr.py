# pytest pre funkciu 'prvocislo_mr'

from main import prvocislo_mr


def test_prvocislo_mr():
    assert prvocislo_mr(1001) is False
    assert prvocislo_mr(1002) is False
    assert prvocislo_mr(1003) is False
    assert prvocislo_mr(1004) is False
    assert prvocislo_mr(1005) is False
    assert prvocislo_mr(1006) is False
    assert prvocislo_mr(1007) is False
    assert prvocislo_mr(1008) is False
    assert prvocislo_mr(1009) is True
    assert prvocislo_mr(6803) is True
    assert prvocislo_mr(7057) is True
    assert prvocislo_mr(7243) is True
    assert prvocislo_mr(7457) is True
