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
    def test_select_race_elf(self, mock_race, mock_output):
        expected = "elf"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=2)
    def test_select_race_halfling(self, mock_race, mock_output):
        expected = "halfling"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=3)
    def test_select_race_tiefling(self, mock_race, mock_output):
        expected = "tiefling"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=4)
    def test_select_race_dragonborn(self, mock_race, mock_output):
        expected = "dragonborn"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=5)
    def test_select_race_dwarf(self, mock_race, mock_output):
        expected = "dwarf"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=6)
    def test_select_race_gnome(self, mock_race, mock_output):
        expected = "gnome"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=7)
    def test_select_race_halfelf(self, mock_race, mock_output):
        expected = "half-elf"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=8)
    def test_select_race_human(self, mock_race, mock_output):
        expected = "human"
        select_race()
        self.assertEqual(expected, select_race())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=9)
    def test_select_race_halforc(self, mock_race, mock_output):
        expected = "half-orc"
        select_race()
        self.assertEqual(expected, select_race())
