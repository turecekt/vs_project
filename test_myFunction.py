import unittest
import reakcniRychlost

def myFunction_False(a, b, c):
    return False, 1.2

class tests(unittest.TestCase):
    def test_myFunction_False(self):
        reakcniRychlost.question = myFunction_False
        reakcniRychlost.myFunction()
    

if __name__ == '__main__':
    unittest.main()
