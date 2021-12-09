import unittest
from main import rimskeCislice


class TestRimskeCislice(unittest.TestCase):
    def testRimskeCislice23(self):
        self.assertEqual(rimskeCislice(23), "XXIII")

    def testRimskeCislice1234(self):
        self.assertEqual(rimskeCislice(1234), "MCCXXXIV")
