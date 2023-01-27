# pytest pre funkciu 'prvocislo'

from main import prvocislo


def test_prvocislo():
        assert prvocislo(1) == False
        assert prvocislo(2) == True
        assert prvocislo(3) == True
        assert prvocislo(4) == False
        assert prvocislo(5) == True
        assert prvocislo(6) == False
        assert prvocislo(7) == True
        assert prvocislo(8) == False
        assert prvocislo(9) == False
        assert prvocislo(10) == False
        assert prvocislo(11) == True
        assert prvocislo(12) == False
        assert prvocislo(13) == True
        assert prvocislo(17) == True
        assert prvocislo(19) == True
        assert prvocislo(149) == True
        assert prvocislo(151) == True
        assert prvocislo(317) == True
        assert prvocislo(577) == True
        assert prvocislo(977) == True
        assert prvocislo(983) == True
        assert prvocislo(991) == True
        assert prvocislo(919) == True
        assert prvocislo(929) == True
        assert prvocislo(937) == True
        assert prvocislo(983) ==  True




