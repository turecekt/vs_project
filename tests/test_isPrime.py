from isPrime import isPrime
import unittest
import time
import datetime
import sympy


class TestIsPrime(unittest.TestCase):
    def test_range(self):
        upto = 100000
        start = time.time()
        for i in range(1, upto+1):
            eta = datetime.timedelta(seconds=(time.time()-start)*(upto-i)/i)
            print(
                "\r Running tests %d/" % i
                + "%d" % upto + " [%f%%]" % (i/upto * 100)
                + ", eta %s" % str(eta),
                end=""
            )

            self.assertEqual(isPrime(i), sympy.isprime(i))


if __name__ == '__main__':
    unittest.main()
