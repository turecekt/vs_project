"""Unittestování k morseove abecede."""
import unittest


"""Unit testy pro morseovku a jeji stringove fce."""
"""Vytvoření testovací třídy class."""


class Tests(unittest.TestCase):
    """Vytvoření třídy."""

    def test_upper(self): """Test na fce zvětšení písmena."""
        self.assertEqual("abc".upper(), "ABC")

    def test_isupper(self): """Testování fce zvětšení písmena."""
        self.assertTrue("ABC".isupper())
        self.assertFalse("Abc".isupper())

    def test_split(self): """Testování fce split."""
        s = "miroslav olivik"
        self.assertEqual(s.split(), ["miroslav", "olivik"])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
