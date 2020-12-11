"""These are unit tests for the main functions of the "calclulator".
"""
import unittest
import calculator


class TestCalculator(unittest.TestCase):
    """Class for unit testing the functions.
    """
    def test_add(self):
        """Test the add function.

        Input of the test are two numbers.

        Output of the test is a addition of two numbers.
        """
        self.assertEqual(calculator.add(20, 10), 30)
        self.assertEqual(calculator.add(-40, 10), -30)
        self.assertEqual(calculator.add(-5, -5), -10)

        
    def test_subtract(self):
        """Test the subtract function.

        Input of the test are two numbers.

        Output of the test is a subtraction of two numbers.
        """
        self.assertEqual(calculator.subtract(20, 10), 10)
        self.assertEqual(calculator.subtract(-40, 10), -50)
        self.assertEqual(calculator.subtract(-5, -5), 0)

        
    def test_multiply(self):
        """Test the multiply function.

        Input of the test are two numbers.

        Output of the test is a multiplication of two numbers.
        """
        self.assertEqual(calculator.multiply(20, 10), 200)
        self.assertEqual(calculator.multiply(-40, 10), -400)
        self.assertEqual(calculator.multiply(-5, -5), 25)

        
    def test_divide(self):
        """Test the divide function.

        Input of the test are two numbers.

        Output of the test is a division of two numbers.
        """
        self.assertEqual(calculator.divide(20, 10), 2)
        self.assertEqual(calculator.divide(-40, 10), -4)
        self.assertEqual(calculator.divide(-5, -5), 1)

        with self.assertRaises(ValueError):
            calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
