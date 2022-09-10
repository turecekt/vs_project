"""Run triangle tests"""
import unittest
import triangle

class SimpleTest(unittest.TestCase):
	"""Very basic example test"""
	# Returns True or False.
	def test(self):
		test_args = ['.\\main.py', '1', '2', '3', '4', '5', '6']
		test_output = "Points are ('1', '2') ('3', '4') ('5', '6')"
		self.assertEqual(triangle.start(test_args),test_output)

if __name__ == '__main__':
	unittest.main()