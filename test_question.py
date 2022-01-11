import unittest
import reakcniRychlost

def autoInput():
    return 5

class tests_question(unittest.TestCase):
    def test_question_correct(self):
        reakcniRychlost.user_input = autoInput
        reakcniRychlost.question(2, 3, "+")

    def test_question_wrong(self):
        reakcniRychlost.user_input = autoInput
        reakcniRychlost.question(2, 0, "+")

    def test_question_err(self):
        reakcniRychlost.user_input = autoInput
        with self.assertRaises(TypeError):
            reakcniRychlost.question(2, "a", "+")
    

if __name__ == '__main__':
    unittest.main()
