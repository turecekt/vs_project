import morse1
import unittest

class Check2(unittest.TestCase):
    known_values = (('.-', 'A'), ('-...', 'B'),
                    ('-.-.', 'C'), ('-..', 'D'),
                    ('.', 'E'), ('..-.', 'F'),
                    ('--.', 'G'),('....', 'H'),
                    ('..', 'I'), ('.---', 'J'),
                    ('-.-', 'K'), ('.-..', 'L'),
                    ('--', 'M'), ('-.', 'N'),
                    ('---', 'O'), ('.--.', 'P'),
                    ('--.-', 'Q'), ('.-.', 'R'),
                    ('...', 'S'), ('-', 'T'),
                    ('..-', 'U'), ('...-', 'V'),
                    ('.--', 'W'), ('-..-', 'X'),
                    ('-.--', 'Y'), ('--..', 'Z'))
    
    def test_decrypt_known_values(self):
        for string, char in self.known_values:
            result = morse1.decrypt(string)
            self.assertEqual(char, result)

if __name__ == '__main__':
    unittest.main()
