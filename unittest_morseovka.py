"""Unit test pro morseovku."""
import unittest
import morseovka


class unittest_morseovka(unittest.TestCase):
	"""Trida pro spusteni unit testu."""

	def test_encrypt_pismeno(self):
		"""Test prevodu pismene na kod."""
		self.assertEqual(morseovka.encrypt("T"), "- ")

	def test_encrypt_veta(self):
		"""Test prevodu vety na kod."""
		self.assertEqual(morseovka.encrypt(
			"TESTOVACI VETA"), "- . ... - --- ...- .- -.-. ..  ...- . - .- ")

	def test_encrypt_cislo(self):
		"""Test prevodu cisla na kod."""
		self.assertEqual(morseovka.encrypt(
			"1234567890"), ".---- ..--- ...-- ....- ....."
			" -.... --... ---.. ----. ----- ")

	def test_decrypt_pismeno(self):
		"""Test prevodu kodu na pismeno."""
		self.assertEqual(morseovka.decrypt("-..-"), "X")

	def test_decrypt_text(self):
		"""Test prevodu kodu na text."""
		self.assertEqual(morseovka.decrypt(
			".--. .-. . ...- --- -..  -. .-  ... .-.."
			" --- ...- ---  --..  -.- --- -.. ..-"),
			"PREVOD NA SLOVO Z KODU")


if __name__ == "main":
	unittest.main()
