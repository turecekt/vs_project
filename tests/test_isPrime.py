import math
import time
import unittest
import sympy
import datetime
from isPrime import isPrime


class TestIsPrime(unittest.TestCase):
    def test_range(self):
        upto=100000
        start=time.time()
        for i in range(1,upto+1):
            print("\r Running tests %d/" % i + "%d" % upto + " [%f%%]" % (i/upto*100) + ", eta %s" % str(datetime.timedelta(seconds=(time.time()-start)*(upto-i)/i)), end="")


            self.assertEqual(isPrime(i), sympy.isprime(i))