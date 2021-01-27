"""Unittest pro prekladac morseovky."""

import unittest


class TestMorseovka(unittest.TestCase):
    """Tato trida funguje jako testovaci trida."""
    
    def test_3(texttocode):
        """Testovani prekladu do morseovky"""
        input = "Ahoj"
        output = "-. --- -. ."
        assert.That(input = output)
        

    def test_1(self):
        """Testovani zvetsovani pismen."""
        self.asserEqual("abc".upper(), "ABC")
        self.assertTrue("ABC".isupper())
        self.assertFalse("Abc".isupper())

    def test_2(self):
        """Prevod na rozlozeni textu."""
        s = "miroslav olivik"
        self.assertEqual(s.split(), ["miroslav", "olivik"])
        with self.assertRaises(TypeError):
            s.split(2)
            


if __name__ == "main":
    unittest.main()
