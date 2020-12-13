import unittest
import projectRom


class MyTestCase(unittest.TestCase):
    def test_deset(self):
        result = projectRom.intToRom(10)
        self.assertEqual(result, 'X')

    def test_jedenact(self):
        result = projectRom.intToRom(11)
        self.assertEqual(result, 'XI')

    def test_stojedenact(self):
        result = projectRom.intToRom(111)
        self.assertEqual(result, 'CXI')

    def test_devet(self):
        result = projectRom.intToRom(9)
        self.assertEqual(result, 'IX')

    def test_nula(self):
        result = projectRom.intToRom(0)
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
