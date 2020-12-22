from unittest import TestCase

from main import zasifrovani


class Test(TestCase):
    def test_main(self):
        self.assertEqual(zasifrovani("SOS"),"... --- ... ", "OK")
