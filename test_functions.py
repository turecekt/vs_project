"""Unittesty funkcí."""

import unittest     # Inport frameworku unittest
import functions    # Inport souboru functions


# Třída pro unittesty na délky stran trojúhelníku
class TestDelkaStrany(unittest.TestCase):
    """Unittest na délku stran AB, BC, AC."""

    """Unittest na délku strany AB"""
    def test_delkaStranyAB(self):
        """#01. unittest pro stranu AB."""
        self.assertEqual(functions.delkaStranyAB(2, 5, 5, 9), 5)
        """#02. unittest pro stranu AB."""
        self.assertEqual(functions.delkaStranyAB(2, -6, -13, -19), 10)
        """#03. unittest pro stranu AB."""
        self.assertEqual(functions.delkaStranyAB(-2.6, -2.6, 119, 130), 11)

    """Unittest na délku strany |BC|."""
    def test_delkaStranyBC(self):
        """#01. unittest pro stranu BC."""
        self.assertEqual(functions.delkaStranyBC(5, 13, 232, 238), 10)
        """#02. unittest pro stranu BC."""
        self.assertEqual(functions.delkaStranyBC(-70, -81, -3, -3), 11)
        """#03. unittest pro stranu BC."""
        self.assertEqual(functions.delkaStranyBC(16, 19, -4, -8), 5)

    """Unittest na délku strany |AC|."""
    def test_delkaStranyAC(self):
        """#01. unittest pro stranu AC."""
        self.assertEqual(functions.delkaStranyAC(-3.38, -3.38, -1, 10), 11)
        """#02. unittest pro stranu AC."""
        self.assertEqual(functions.delkaStranyAC(67, 71, 310, 313), 5)
        """#03. unittest pro stranu AC."""
        self.assertEqual(functions.delkaStranyAC(4, -2, -4, -12), 10)


# Třída pro unittesty na obvod a obsah trojúhelníku
class TestObvodObsah(unittest.TestCase):
    """Unittest na obvod a obsah."""

    """Unittest na obvod"""
    def test_obvod(self):
        """#01. unittest pro obvod."""
        self.assertEqual(functions.obvodTroj(0, 8, 0, 6, 0, 0), 24)
        """#02. unittest pro obvod."""
        self.assertEqual(functions.obvodTroj(0, 3, 0, 4, 0, 0), 12)

    """Unittest na obsah."""
    def test_obsah(self):
        """#01. unittest pro obsah."""
        self.assertEqual(functions.obsahTroj(1, 9, 1, 7, 1, 1), 24)
        """#02. unittest pro obsah."""
        self.assertEqual(functions.obsahTroj(17, 20, 17, 21, 17, 17), 6)


# Třída pro unittest na zkoušku pravoúhlosti
class TestPravouhlosti(unittest.TestCase):
    """Unittest na zkoušku pravoúhlosti."""

    def test_pravouhlosti(self):
        """#01. unittest pro zkoušku pravoúhlosti."""
        self.assertEqual(functions.zkPravouhlosti(0, 3, 0, 4, 0, 0), 1)
        """#02. unittest pro zkoušku pravoúhlosti."""
        self.assertEqual(functions.zkPravouhlosti(-8, 24, 19, 0, -74, 67), 0)
