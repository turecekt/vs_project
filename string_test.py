#unittestování k morseove abecede
import unittest

# unit testy pro morseovku a jeji stringove fce
# vytvoření testovací třídy class


class TestStringMethods(unittest.TestCase):

    # test pro spravnou funkci na zvětšení písmena

    # druhý test na zvětšení písmena

    # třetí test na zjištění správnosti funkce split

    def test_upper(self):
        self.assertEqual("abc".upper(), "ABC")

    def test_isupper(self):
        self.assertTrue("ABC".isupper())
        self.assertFalse("Abc".isupper())

    def test_split(self):
        s = "miroslav olivik"
        self.assertEqual(s.split(), ["miroslav", "olivik"])
        with self.assertRaises(TypeError):
            s.split(2)
 

if __name__ == "__main__":
    unittest.main()
