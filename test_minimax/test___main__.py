import unittest
import unittest.mock
from minimax import __main__ as main


class TestMain(unittest.TestCase):
    def test_parse_args(self):
        with self.subTest(msg="Overenie fungovania parse_args pre nahodne cisla (bez argumentu)"):
            with unittest.mock.patch("minimax.__main__.sys.argv", ["subor"]):
                with unittest.mock.patch("minimax.__main__.random.randint", return_value=1):
                    vysledne_cisla = main.parse_args()
                    # dostaneme 20 nahodnych cisiel, kedze ale randint vzdy vrati 1, dostaneme 20 jednotiek
                    self.assertEqual(vysledne_cisla, [1] * 20)

        with self.subTest(msg="Overenie fungovania parse_args pre zadane cisla (cisla v argumentoch)"):
            ocakavane_cisla = [1, 2, 3]
            with unittest.mock.patch("minimax.__main__.sys.argv", ["subor", "1", "2", "3"]):
                vysledne_cisla = main.parse_args()
                # Dostaneme 1, 2, 3 ako bolo zadane v argumentoch
                self.assertEqual(vysledne_cisla, [1, 2, 3])

        with self.subTest(msg="Overenie fungovania parse_args pre subor (argument je cesta k suboru)."):
            with unittest.mock.patch("minimax.__main__.open", unittest.mock.mock_open(read_data="1 2 3")):
                with unittest.mock.patch("minimax.__main__.sys.argv", ["subor", "subor.txt"]):
                    vysledne_cisla = main.parse_args()
                    # Dostaneme 1, 2, 3 z obsahu suboru
                    self.assertEqual(vysledne_cisla, [1, 2, 3])