# pytest pre funkciu 'prvocislo_mr'

from main import prvocislo_mr


def test_prvocislo_mr(self):
    self.assertFalse(prvocislo_mr(1001))
    self.assertFalse(prvocislo_mr(1002))
    self.assertFalse(prvocislo_mr(1003))
    self.assertFalse(prvocislo_mr(1004))
    self.assertFalse(prvocislo_mr(1005))
    self.assertFalse(prvocislo_mr(1006))
    self.assertFalse(prvocislo_mr(1007))
    self.assertFalse(prvocislo_mr(1008))
    self.assertTrue(prvocislo_mr(1009))
    self.assertTrue(prvocislo_mr(6803))
    self.assertTrue(prvocislo_mr(7057))
    self.assertTrue(prvocislo_mr(7243))
    self.assertTrue(prvocislo_mr(7457))
