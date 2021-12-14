
import morseovka
import unittest

class unittest_morseovka(unittest.TestCase):
	def test_encrypt_pismeno(self):
		self.assertEqual(morseovka.encrypt("T"), "- ")
	def test_encrypt_veta(self):
		self.assertEqual(morseovka.encrypt("TESTOVACI VETA"), "- . ... - --- ...- .- -.-. ..  ...- . - .- ")
	def test_encrypt_cislo(self):
		self.assertEqual(morseovka.encrypt("1234567890"), ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- ")
	def test_decrypt_pismeno(self):
		self.assertEqual(morseovka.decrypt("-..- "), "X")
	def test_decrypt_pismeno(self):
		self.assertEqual(morseovka.decrypt(".--. .-. . ...- --- -..  -. .-  ... .-.. --- ...- ---  --..  -.- --- -.. ..-"), "PREVOD NA SLOVO Z KODU")
	
if __name__ == "main":
	unittest.main()