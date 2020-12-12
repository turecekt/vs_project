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
