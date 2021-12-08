import unittest
from minimax import utils


class TestUtils(unittest.TestCase):
    def test_minimax(self):
        """Otestovanie správnosti funkcie minimax."""
        vysledky = (
            ([1, 8, 0], (0, 2, 8, 1)),
            ([2, 6, 7, 1], (1, 3, 7, 2)),
            ([-9, -470, 32], (-470, 1, 32, 2)),
            ([0], (0, 0, 0, 0)),
            ([7], (7, 0, 7, 0)),
            ([-41, -21, -32], (-41, 0, -21, 1)),
        )

        for list_cisel, ocakavany_vysledok in vysledky:
            with self.subTest(
                msg="Test spravneho vysledku pre minimax funkciu",
                list_cisel=list_cisel
            ):
                obdrzany_vysledok = utils.minimax(list_cisel)
                self.assertEqual(ocakavany_vysledok, obdrzany_vysledok)

    def test_bubble_sort(self):
        """Otestovanie správnosti funkcie bubble_sort."""
        vysledky = (
            ([1, 8, 4], [1, 4, 8]),
            ([2, 16, 40, 1, -14], [-14, 1, 2, 16, 40]),
            ([-80, -22, -11, -55], [-80, -55, -22, -11]),
            ([0, 1, 2, 3, 4, -6], [-6, 0, 1, 2, 3, 4]),
            ([5], [5]),
            ([100, -10, 200, -20], [-20, -10, 100, 200]),
        )

        for list_cisel, ocakavany_vysledok in vysledky:
            with self.subTest(
                msg="Test spravneho vysledku pre bubble_sort funkciu",
                list_cisel=list_cisel
            ):
                obdrzany_vysledok = utils.bubble_sort(list_cisel)
                self.assertEqual(ocakavany_vysledok, obdrzany_vysledok)

    def quick_sort(self):
        """Otestovanie správnosti funkcie quick_sort."""
        vysledky = (
            ([1, 8, 4], [1, 4, 8]),
            ([2, 16, 40, 1, -14], [-14, 1, 2, 16, 40]),
            ([-80, -22, -11, -55], [-80, -55, -22, -11]),
            ([0, 1, 2, 3, 4, -6], [-6, 0, 1, 2, 3, 4]),
            ([5], [5]),
            ([100, -10, 200, -20], [-20, -10, 100, 200]),
        )

        for list_cisel, ocakavany_vysledok in vysledky:
            with self.subTest(
                msg="Test spravneho vysledku pre quick_sort funkciu",
                list_cisel=list_cisel
            ):
                obdrzany_vysledok = utils.quick_sort(list_cisel)
                self.assertEqual(ocakavany_vysledok, obdrzany_vysledok)

    def insertion_sort(self):
        """Otestovanie správnosti funkcie insertion_sort."""
        vysledky = (
            ([1, 8, 4], [1, 4, 8]),
            ([2, 16, 40, 1, -14], [-14, 1, 2, 16, 40]),
            ([-80, -22, -11, -55], [-80, -55, -22, -11]),
            ([0, 1, 2, 3, 4, -6], [-6, 0, 1, 2, 3, 4]),
            ([5], [5]),
            ([100, -10, 200, -20], [-20, -10, 100, 200]),
        )

        for list_cisel, ocakavany_vysledok in vysledky:
            with self.subTest(
                msg="Test spravneho vysledku pre insertion_sort funkciu",
                list_cisel=list_cisel
            ):
                obdrzany_vysledok = utils.insertion_sort(list_cisel)
                self.assertEqual(ocakavany_vysledok, obdrzany_vysledok)
