import unittest
from Morseovka import TextToMorse
from Morseovka import MorseToText

        # text na Moresuv kod
class Test(unittest.TestCase):

      def test_prelozeni(self):
        self.assertEqual(TextToMorse('asd'), ' .- ... -..')
      def test_spravnych_symbolu(self):
        self.assertEqual(TextToMorse('!`@#$%^&()+='), 'nespravne znaky')
      def test_prazdneho_pole(self):
        self.assertEqual(TextToMorse(''), 'prazdne pole')

        # Moresuv kod na text
class Test1(unittest.TestCase):
      def test_prelozeni(self):
         self.assertEqual(MorseToText(['...', '---', '...']), 'sos')
      def test_textu_v_sp(self):
          self.assertEqual(MorseToText(['----------']), 'chyba pri zadavani znaku' )
      def test_spravnych_symbolu(self):
          self.assertEqual(MorseToText(['!@#$%^&()+']),'nespravne znaky')
      def test_prazdneho_pole(self):
        self.assertEqual(MorseToText(''), 'prazdne pole')


if __name__ == '__main__':
    unittest.main()