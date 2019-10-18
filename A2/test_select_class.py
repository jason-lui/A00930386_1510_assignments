from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import select_class
import io

class TestSelect_class(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=1)
    def test_select_class_print(self, mock_class, mock_output):
        expected = """Select a class:
1. Fighter
2. Wizard
3. Cleric
4. Rogue
5. Ranger
6. Barbarian
7. Bard
8. Druid
9. Monk
10. Paladin
11. Sorcerer
12. Warlock
"""
        select_class()
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=1)
    def test_select_class_fighter(self, mock_class, mock_output):
        expected = "fighter"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=2)
    def test_select_class_wizard(self, mock_class, mock_output):
        expected = "wizard"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=3)
    def test_select_class_cleric(self, mock_class, mock_output):
        expected = "cleric"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=4)
    def test_select_class_rogue(self, mock_class, mock_output):
        expected = "rogue"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=5)
    def test_select_class_ranger(self, mock_class, mock_output):
        expected = "ranger"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=6)
    def test_select_class_barbarian(self, mock_class, mock_output):
        expected = "barbarian"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=7)
    def test_select_class_bard(self, mock_class, mock_output):
        expected = "bard"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=8)
    def test_select_class_druid(self, mock_class, mock_output):
        expected = "druid"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=9)
    def test_select_class_monk(self, mock_class, mock_output):
        expected = "monk"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=10)
    def test_select_class_paladin(self, mock_class, mock_output):
        expected = "paladin"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=11)
    def test_select_class_sorcerer(self, mock_class, mock_output):
        expected = "sorcerer"
        select_class()
        self.assertEqual(expected, select_class())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=12)
    def test_select_class_warlock(self, mock_class, mock_output):
        expected = "warlock"
        select_class()
        self.assertEqual(expected, select_class())
