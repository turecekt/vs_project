# pytest pre funkciu 'prvocislo'

from main import prvocislo


def test_prvocislo(self):
    self.assertFalse(prvocislo(1))
    self.assertTrue(prvocislo(2))
    self.assertTrue(prvocislo(3))
    self.assertFalse(prvocislo(4))
    self.assertTrue(prvocislo(5))
    self.assertFalse(prvocislo(6))
    self.assertTrue(prvocislo(149))
    self.assertTrue(prvocislo(151))
    self.assertTrue(prvocislo(317))
    self.assertTrue(prvocislo(577))
    self.assertTrue(prvocislo(977))
    self.assertTrue(prvocislo(983))
    self.assertTrue(prvocislo(991))
    self.assertTrue(prvocislo(919))
    self.assertTrue(prvocislo(929))
    self.assertTrue(prvocislo(937))
    self.assertTrue(prvocislo(983))
