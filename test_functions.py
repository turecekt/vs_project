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
