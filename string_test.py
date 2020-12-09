# !/usr/bin/en v python3

# unit testy pro morseovku a jeji stringove fce

import unittest


class TestStringMethods(unittest.TestCase): 


# test pro spravnou funkci na zvětšení písmena

    def test_upper(self):
        self.assertEqual("abc".upper(), "ABC")
      
# druhý test na zvětšení písmena


    def test_isupper(self):
        self.assertTrue("ABC".isupper())
        self.assertFalse("Abc".isupper())
 

# test na zjištění správnosti funkce split


    def test_split(self):
        s = "miroslav olivik"
        self.assertEqual(s.split(), ["miroslav", "olivik"])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()

