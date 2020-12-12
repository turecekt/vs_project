"""Unittestování k morseove abecede."""
import unittest


"""Unit testy pro morseovku a jeji stringove fce."""
"""Vytvoření testovací třídy class."""


class Tests(unittest.TestCase):
    """Vytvoření třídy."""
    
    def test_upper(vlastni): """Test na fce zvětšení písmena."""
    vlastni.assertEqual("abc".upper(), "ABC")

    def test_isupper(vlastni): """Testování fce zvětšení písmena."""
    vlastni.assertTrue("ABC".isupper())
    vlastni.assertFalse("Abc".isupper())

    def test_split(vlastni): """Testování fce split."""
    s = "miroslav olivik"
    vlastni.assertEqual(s.split(), ["miroslav", "olivik"])
    with vlastni.assertRaises(TypeError):
        s.split(2)


if __name__ == '__main__':
    unittest.main()
