import morse1
import unittest

class Check(unittest.TestCase):
    known_values = (('A','.-'), ('B','-...'),
                    ('C','-.-.'), ('D','-..'),
                    ('E','.'), ('F','..-.'),
                    ('G','--.'), ('H','....'),
                    ('I','..'), ('J','.---'),
                    ('K','-.-'), ('L','.-..'),
                    ('M','--'), ('N','-.'),
                    ('O','---'), ('P','.--.'),
                    ('Q','--.-'), ('R','.-.'),
                    ('S','...'), ('T','-'),
                    ('U','..-'), ('V','...-'),
                    ('W','.--'), ('X','-..-'),
                    ('Y','-.--'), ('Z','--..'),
                    (' ', ''))
    
 
    def test_encrypt_known_values(self):
        
        """
        Snad už to bude fungovat.
        
        Dvě funkce. Jedna pro zakódování(encrypt), jedna pro překlad(decrypt).
        """
        
        for char, string in self.known_values:
            result = morse1.encrypt(char)
            self.assertEqual(string, result)

if __name__ == '__main__':
    unittest.main()
