import unittest
from reakcniRychlost import myFunction

class tests_myFunction(unittest.TestCase):

    def test_myFunction(monkeypatch):

        monkeypatch.setattr('builtins.input', lambda _: 5)
        myFunction()
    #assert i == "XXX"
    
    

if __name__ == '__main__':
    unittest.main()
