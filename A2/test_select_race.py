from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import select_race
import io


class TestSelect_race(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=1)
    def test_select_race_print(self, mock_race, mock_output):
        expected = """Select a race:
1. Elf
2. Halfling
3. Tiefling
4. Dragonborn
5. Dwarf
6. Gnome
7. Half-Elf
8. Human
9. Half-Orc
"""
        select_race()
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=1)
    def test_select_race(self, mock_race, mock_output):
        expected = "fighter"
        select_race()
        self.assertEqual(expected, select_race())