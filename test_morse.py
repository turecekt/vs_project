import unittest

import morse


class Test(unittest.TestCase):

    # Morseova abeceda na text
    def test_morse_na_cisla(self):
        prekladac = main.decrypt(".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----")
        self.assertEqual(prekladac, "1234567890")

    def test_morse_na_text(self):
        prekladac = main.decrypt(".- .... --- .---  ... ...- . - ")
        self.assertEqual(prekladac, "AHOJ SVET ")

    def test_morse_na_znaky(self):
        prekladac = main.decrypt(".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. "
                                 "..--.. -..-. ")
        self.assertEqual(prekladac, "&'@)(:,=!.-+?/ ")

    # Text na morseovu abecedu
    def test_cisla_na_morse(self):
        prekladac = main.encrypt("1234567890")
        self.assertEqual(prekladac, ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- ")

    def test_text_na_morse(self):
        prekladac = main.encrypt("AHOJ SVET ")
        self.assertEqual(prekladac, ".- .... --- .---  ... ...- . -  ")

    def test_vsetko_na_morse(self):
        prekladac = main.encrypt("AHOJ 123 SVET 3909")
        self.assertEqual(prekladac, ".- .... --- .---  .---- ..--- ...--  ... ...- . -  ...-- ----. ----- ----. ")

    def test_znaky_na_morse(self):
        prekladac = main.encrypt("&'@)(:,=!.-+?/")
        self.assertEqual(prekladac, ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. "
                                    "..--.. -..-. ")


if __name__ == "__main__":
    unittest.main()
