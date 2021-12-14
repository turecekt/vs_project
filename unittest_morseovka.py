"""Adfhdfh."""
import unittest
import morseovka


class unittest_morseovka(unittest.TestCase):
	"""Ahoj."""

	def test_encrypt_pismeno(self):
		"""Ahoj."""
		self.assertEqual(morseovka.encrypt("T"), "- ")

	def test_encrypt_veta(self):
		"""Ahoj."""
		self.assertEqual(morseovka.encrypt(
			"TESTOVACI VETA"), "- . ... - --- ...- .- -.-. ..  ...- . - .- ")

	def test_encrypt_cislo(self):
		"""Ahoj."""
		self.assertEqual(morseovka.encrypt(
			"1234567890"), ".---- ..--- ...-- ....- ....."
			" -.... --... ---.. ----. ----- ")

	def test_decrypt_pismeno(self):
		"""Ahoj."""
		self.assertEqual(morseovka.decrypt("-..-"), "X")

	def test_decrypt_text(self):
		"""Ahoj."""
		self.assertEqual(morseovka.decrypt(
			".--. .-. . ...- --- -..  -. .-  ... .-.."
			" --- ...- ---  --..  -.- --- -.. ..-"),
			"PREVOD NA SLOVO Z KODU")


if __name__ == "main":
	unittest.main()
