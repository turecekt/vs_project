"""unittestování k morseove abecede"""
import unittest


# unit testy pro morseovku a jeji stringove fce
# vytvoření testovací třídy class


class TestStringMethods(unittest.TestCase):
"""vytvoření třídy pro testování"""

    def test_upper(self):
        self.assertEqual("abc".upper(), "ABC")
        """testování fce zvětšení písmena"""

    def test_isupper(self):
        self.assertTrue("ABC".isupper())
        self.assertFalse("Abc".isupper())
        """testování fce zvětšení písmena"""

    def test_split(self):
        s = "miroslav olivik"
        self.assertEqual(s.split(), ["miroslav", "olivik"])
        with self.assertRaises(TypeError):
            s.split(2)
            """testování fce split"""


if __name__ == "__main__":
    unittest.main()
