"""unittestování k morseove abecede."""
import unittest


"""unit testy pro morseovku a jeji stringove fce."""
"""vytvoření testovací třídy class."""


class TestStringMethods(unittest.TestCase):
    """vytvoření třídy pro testování."""


def test_upper(vlastni): """testování fce zvětšení písmena."""

    
vlastni.assertEqual("abc".upper(), "ABC")


def test_isupper(vlastni): """testování fce zvětšení písmena."""


vlastni.assertTrue("ABC".isupper())
vlastni.assertFalse("Abc".isupper())


def test_split(vlastni): """testování fce split."""


s = "miroslav olivik"
vlastni.assertEqual(s.split(), ["miroslav", "olivik"])
with vlastni.assertRaises(TypeError):
    s.split(2)


if __name__ == "__main__":
    unittest.main()
