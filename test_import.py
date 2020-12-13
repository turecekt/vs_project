"""Import unit testy k projektu"""
import unittest
import projectRom


class MyTestCase(unittest.TestCase):
    """Vytvoreni class a funkce na pytesty"""
    def test_deset(self):
        """Vytvoreni testu ktery testne input 10"""
        result = projectRom.intToRom(10)
        self.assertEqual(result, 'X')

    def test_jedenact(self):
        """Vytvoreni testu ktery testne 11"""
        result = projectRom.intToRom(11)
        self.assertEqual(result, 'XI')

    def test_stojedenact(self):
        """Vytvoreni testu ktery testne 111"""
        result = projectRom.intToRom(111)
        self.assertEqual(result, 'CXI')

    def test_devet(self):
        """Vytvoreni testu ktery tesne 9"""
        result = projectRom.intToRom(9)
        self.assertEqual(result, 'IX')

    def test_nula(self):
        """Vytvoreni testu ktery tesne 0"""
        result = projectRom.intToRom(0)
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
