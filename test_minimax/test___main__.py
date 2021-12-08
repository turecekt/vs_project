"""Tento subor obsahuje testy pre minimax/__main__.py."""

import unittest
import unittest.mock
from minimax import __main__ as main
from minimax import utils


class TestMain(unittest.TestCase):
    """Tato trieda obsahuje funkcie pre testovanie __main__ suboru."""

    def test_parse_args(self):
        """Otestovanie správnosti funkcie parse_args."""
        with self.subTest(msg="Overenie fungovania parse_args pre nahodne cisla (bez arg)"):
            with unittest.mock.patch("minimax.__main__.sys.argv", ["subor"]):
                with unittest.mock.patch("minimax.__main__.random.randint", return_value=1):
                    vysledne_cisla = main.parse_args()
                    # dostaneme 20 nahodnych cisiel,
                    # kedze ale randint vzdy vrati 1, dostaneme 20 jednotiek
                    self.assertEqual(vysledne_cisla, [1] * 20)

        with self.subTest(msg="Overenie fungovania parse_args pre zadane cisla (cisla v arg)"):
            with unittest.mock.patch("minimax.__main__.sys.argv", ["subor", "1", "2", "3"]):
                vysledne_cisla = main.parse_args()
                # Dostaneme 1, 2, 3 ako bolo zadane v argumentoch
                self.assertEqual(vysledne_cisla, [1, 2, 3])

        with self.subTest(msg="Overenie fungovania parse_args pre subor (arg je cesta k suboru)."):
            with unittest.mock.patch(
                "minimax.__main__.open", unittest.mock.mock_open(read_data="1 2 3")
            ):
                with unittest.mock.patch("minimax.__main__.sys.argv", ["subor", "subor.txt"]):
                    vysledne_cisla = main.parse_args()
                    # Dostaneme 1, 2, 3 z obsahu suboru
                    self.assertEqual(vysledne_cisla, [1, 2, 3])

    def test_vyber_algoritmus(self):
        """Otestovanie správnosti funkcie vyber_algoritmus."""
        vysledky = (
            ("1", utils.quick_sort),
            ("2", utils.bubble_sort),
            ("3", utils.insertion_sort),
            ("4", sorted),
        )

        for cislo, ocakavany_vysledok in vysledky:
            with unittest.mock.patch("minimax.__main__.input", return_value=cislo):
                with self.subTest(
                    msg="Test spravneho vysledku pre vyber_algoritmus funkciu",
                    cislo=cislo
                ):
                    obdrzany_vysledok = main.vyber_algoritmus()
                    self.assertEqual(ocakavany_vysledok, obdrzany_vysledok)
