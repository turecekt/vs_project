import unittest
from project import romanNum

class testOutput(unittest.TestCase):
    def test_deset(self):
        translator = romanNum()
        userInp = 10
        expected_output = 'X'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def test_nul(self):
        translator = romanNum()
        userInp = 0
        expected_output = ''
        self.assertEqual(translator.intToRom(userInp), expected_output)


    def test_tisicJedna(self):
        translator = romanNum()
        userInp = 1001
        expected_output = 'MI'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def test_devetDevetDevet(self):
        translator = romanNum()
        userInp = 999
        expected_output = 'CMXCIX'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def test_dvaTisiceJedna(self):
        translator = romanNum()
        userInp = 2001
        expected_output = 'MMI'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def test_jedenact(self):
        translator = romanNum()
        userInp = 1
        expected_output = 'XI'
        self.assertEqual(translator.intToRom(userInp), expected_output)





if __name__ == '__main__':
    unittest.main()
