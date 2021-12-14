
import morseovka
import unittest

class unittest_morseovka(unittest.TestCase):
	def test_encrypt_pismeno(self):
		self.assertEqual(morseovka.encrypt("T"), "- ")
	def test_encrypt_veta(self):
		self.assertEqual(morseovka.encrypt("TESTOVACI VETA"), "- . ... - --- ...- .- -.-. ..  ...- . - .- ")

if __name__ == "main":
	unittest.main()