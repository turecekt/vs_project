import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(20, 10), 30)
        self.assertEqual(calculator.add(-40, 10), -30)
        self.assertEqual(calculator.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(20, 10), 10)
        self.assertEqual(calculator.subtract(-40, 10), -50)
        self.assertEqual(calculator.subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(20, 10), 200)
        self.assertEqual(calculator.multiply(-40, 10), -400)
        self.assertEqual(calculator.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(calculator.divide(20, 10), 2)
        self.assertEqual(calculator.divide(-40, 10), -4)
        self.assertEqual(calculator.divide(-5, -5), 1)

        with self.assertRaises(ValueError):
            calculator.divide(10,0)


if __name__ == "__main__":
    unittest.main()
