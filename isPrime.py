import math
import time
import unittest
import sympy
import datetime

def isPrime(n):
    # start = time.time()

    # def printTime(start):
        # print("\rFinished in %f seconds" % (time.time() - start))

    if n <= 1:
        # printTime(start)
        return False
    if n <= 3:
        # printTime(start)
        return True
    if n % 2 == 0 or n % 3 == 0:
        # printTime(start)
        return False
    i = 5
    while i * i <= n:
        progress = i*i/n
        # print("\r%f%%" % (i*i/n*100), end="")

        if n % i == 0 or n % (i + 2) == 0:
            # printTime(start)
            return False
        i += 6

    # printTime(start)
    return True

class TestIsPrime(unittest.TestCase):
    def test_range(self):
        upto=100000
        start=time.time()
        for i in range(1,upto+1):
            print("\r Running tests %d/" % i + "%d" % upto + " [%f%%]" % (i/upto*100) + ", eta %s" % str(datetime.timedelta(seconds=(time.time()-start)*(upto-i)/i)), end="")


            self.assertEqual(isPrime(i), sympy.isprime(i))


if __name__ == '__main__':
    unittest.main()
