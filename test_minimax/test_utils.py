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
                obdrzany_vysledok = utils.minimax(list_cisel)
                self.assertEqual(ocakavany_vysledok, obdrzany_vysledok)

    def test_bubble_sort(self):
        """Otestovanie správnosti funkcie bubblesort."""
        vysledky = (
            ([1, 8, 4], [1, 4, 8]),
        )

        for list_cisel, ocakavany_vysledok in vysledky:
                obdrzany_vysledok = utils.bubble_sort(list_cisel)
                self.assertEqual(ocakavany_vysledok, obdrzany_vysledok)