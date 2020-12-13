# import class source_test pro testování a unittestingu
import unittest
import source_test

# Testovácí class
class TestMorseovky(unittest.TestCase):


    # PŘEVODY Z ABECEDY DO MORSEOVKY
    # jen písmena všechna mala
    def test_1(self):
        result = source_test.prevod("sos")
        self.assertEqual(result, "... --- ... ")

    # jen písmena všechna velká
    def test_2(self):
        result = source_test.prevod("AHOJ")
        self.assertEqual(result, ".- .... --- .--- ")

    # kombinace velkých a malých písmen
    def test_3(self):
        result = source_test.prevod("AhOj")
        self.assertEqual(result, ".- .... --- .--- ")

    # jen čísla
    def test_4(self):
        result = source_test.prevod("365")
        self.assertEqual(result, "...-- -.... ..... ")

    # čísla a písmena
    def test_5(self):
        result = source_test.prevod("Mam 20 let")
        self.assertEqual(result, "-- .- --   ..--- -----   .-.. . - ")

    # PŘEVODY Z MORSEOVKY DO ABECEDY
    # jen písmena
    def test_6(self):
        result = source_test.prevod(".- .... --- .---")
        self.assertEqual(result, "AHOJ")

    # jen čísla
    def test_7(self):
        result = source_test.prevod("...-- -.... .....")
        self.assertEqual(result, "365")

    # čísla a písmena
    def test_8(self):
        result = source_test.prevod("-- .- -- ..--- ----- .-.. . -")
        self.assertEqual(result, "MAM20LET")

if __name__ == '__main__':
    unittest.main()
