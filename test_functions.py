"""Unittesty funkcí."""

# Inport frameworku unittest a souboru functions
import unittest
import functions

# Rychlý způsob, jak napsat modul, který jde jak importovat, tak spustit
if __name__ == '__main__':
    unittest.main()


# Třída pro unittesty na délky stran trojúhelníku
class TestDelkaStrany(unittest.TestCase):
    """Unittest na délku stran AB, BC, AC."""

    """Unittest na délku strany AB"""
    def test_delkaStranyAB(self):
        """Unittesty pro stranu AB."""
        self.assertEqual(functions.delkaStranyAB(2, 5, 5, 9), 5)
        self.assertEqual(functions.delkaStranyAB(2, -6, -13, -19), 10)
        self.assertEqual(functions.delkaStranyAB(-2.6, -2.6, 119, 130), 11)

    """Unittest na délku strany |BC|."""
    def test_delkaStranyBC(self):
        """Unittesty pro stranu BC."""
        self.assertEqual(functions.delkaStranyBC(5, 13, 232, 238), 10)
        self.assertEqual(functions.delkaStranyBC(-70, -81, -3, -3), 11)
        self.assertEqual(functions.delkaStranyBC(16, 19, -4, -8), 5)

    """Unittest na délku strany |AC|."""
    def test_delkaStranyAC(self):
        """Unittesty pro stranu AC."""
        self.assertEqual(functions.delkaStranyAC(-3.38, -3.38, -1, 10), 11)
        self.assertEqual(functions.delkaStranyAC(67, 71, 310, 313), 5)
        self.assertEqual(functions.delkaStranyAC(4, -2, -4, -12), 10)


# Třída pro unittesty na obvod a obsah trojúhelníku
class TestObvodObsah(unittest.TestCase):
    """Unittest na obvod a obsah."""

    """Unittest na obvod"""
    def test_obvod(self):
        """Unittesty pro obvod."""
        self.assertEqual(functions.obvodTroj(0, 8, 0, 6, 0, 0), 24)
        self.assertEqual(functions.obvodTroj(0, 3, 0, 4, 0, 0), 12)
