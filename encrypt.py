"""
Snad už to bude fungovat.

Dvě funkce. Jedna pro zakódování(encrypt), jedna pro překlad(decrypt).
"""
import morse1
import unittest


"""
Snad už to bude fungovat.

Dvě funkce. Jedna pro zakódování(encrypt), jedna pro překlad(decrypt).
"""


class Check(unittest.TestCase):
    """Slovník."""

    known_values = (('A', '.-'), ('B', '-...'),
                    ('C', '-.-.'), ('D', '-..'),
                    ('E', '.'), ('F', '..-.'),
                    ('G', '--.'), ('H', '....'),
                    ('I', '..'), ('J', '.---'),
                    ('K', '-.-'), ('L', '.-..'),
                    ('M', '--'), ('N', '-.'),
                    ('O', '---'), ('P', '.--.'),
                    ('Q', '--.-'), ('R', '.-.'),
                    ('S', '...'), ('T', '-'),
                    ('U', '..-'), ('V', '...-'),
                    ('W', '.--'), ('X', '-..-'),
                    ('Y', '-.--'), ('Z', '--..'),
                    (' ', ''))
   

    def test_encrypt_known_values(self):
        for char, string in self.known_values:
            result = morse1.encrypt(char)
            self.assertEqual(string, result)

if __name__ == '__main__':
    unittest.main()
