# pytest pre funkciu 'prvocislo_mr'

from main import prvocislo_mr

def test_prvocislo_mr():
    assert prvocislo_mr(1001) == False
    assert prvocislo_mr(1002) == False
    assert prvocislo_mr(1003) == False
    assert prvocislo_mr(1004) == False
    assert prvocislo_mr(1005) == False
    assert prvocislo_mr(1006) == False
    assert prvocislo_mr(1007) == False
    assert prvocislo_mr(1008) == False
    assert prvocislo_mr(1009) == True
    assert prvocislo_mr(6803) == True
    assert prvocislo_mr(7057) == True
    assert prvocislo_mr(7243) == True
    assert prvocislo_mr(7457) == True

