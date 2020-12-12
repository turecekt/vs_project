"""unittestování k morseove abecede."""
import unittest


"""unit testy pro morseovku a jeji stringove fce."""
"""vytvoření testovací třídy class."""


class TestStringMethods(unittest.TestCase):
    """vytvoření třídy pro testování."""


def test_upper(self): # noqua: F821
    """testování fce zvětšení písmena."""


self.assertEqual("abc".upper(), "ABC")


def test_isupper(self): # noqua: F821
    """testování fce zvětšení písmena."""


self.assertTrue("ABC".isupper())
self.assertFalse("Abc".isupper())


def test_split(self): # noqua: F821
    """testování fce split."""


s = "miroslav olivik"
self.assertEqual(s.split(), ["miroslav", "olivik"])
with self.assertRaises(TypeError):
    s.split(2)


if __name__ == "__main__": 
    unittest.main()
