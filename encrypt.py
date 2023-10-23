"""
Test funkce encrypt.

Import kódu morse1, který obsahuje testovanou funkci a unittestu.
"""
import morse1
import unittest


"""
Test funkce encrypt.

Testování správnosti zakódování textu.
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
        """Test."""
        for char, string in self.known_values:
            result = morse1.encrypt(char)
            self.assertEqual(string, result)


if __name__ == '__main__':
    unittest.main()
