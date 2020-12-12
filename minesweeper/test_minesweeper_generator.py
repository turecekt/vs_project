from minesweeper import minesweeper_generator
from unittest import TestCase
from unittest.mock import patch, call


class TestCheckInput(TestCase):
    def test_check_input_non_numeric_input(self):
        self.assertFalse(minesweeper_generator.check_input("jrif"))

